pipeline {
  agent any
  environment {
    IMAGE = "shivzankar/bg-app"
    TAG   = "${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Build & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                         usernameVariable: 'U', passwordVariable: 'P')]) {
          sh '''
            docker build -t $IMAGE:$TAG .
            echo $P | docker login -u $U --password-stdin
            docker push $IMAGE:$TAG
          '''
        }
      }
    }

    stage('Detect Live Color') {
      steps {
        script {
          env.LIVE = sh(returnStdout: true, script:
            "kubectl get svc bg-app-svc -o jsonpath='{.spec.selector.version}' 2>/dev/null || echo none").trim()
          env.IDLE = (env.LIVE == 'blue') ? 'green' : 'blue'
          echo "LIVE = ${env.LIVE}  ->  deploying new version to ${env.IDLE}"
        }
      }
    }

    stage('Deploy to Idle Environment') {
      steps {
        sh '''
          sed -e "s|__COLOR__|$IDLE|g" -e "s|__TAG__|$TAG|g" -e "s|IMAGE_PLACEHOLDER|$IMAGE:$TAG|" \
              k8s/deployment-template.yaml | kubectl apply -f -
          kubectl rollout status deployment/app-$IDLE --timeout=180s
        '''
      }
    }

    stage('Smoke Test') {
      steps {
        sh 'kubectl run smoke-$BUILD_NUMBER --rm -i --restart=Never --image=curlimages/curl -- curl -fs http://app-$IDLE-svc/health'
      }
    }

    stage('Approve Switch') {
      steps { input message: "Switch live traffic to ${env.IDLE}?" }
    }

    stage('Switch Traffic') {
      steps {
        sh '''
          kubectl get svc bg-app-svc || kubectl apply -f k8s/service.yaml
          kubectl patch svc bg-app-svc -p '{"spec":{"selector":{"app":"bg-app","version":"'"$IDLE"'"}}}'
          echo "Traffic switched to $IDLE. Old color ($LIVE) kept running for instant rollback."
        '''
      }
    }
  }
  post {
    failure { echo "Deployment failed - live traffic was NOT switched; users unaffected." }
    always  { sh 'docker logout || true' }
  }
}
