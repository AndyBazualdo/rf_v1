pipeline {
    agent { label 'master'}
    stages {
        stage('local docker image') {
            agent {
                 docker { image 'gato756/rf_v1:latest' }
            }
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh "robot /home/andy/tests/Outlook/test1.robot"
            }
        }
        stage('local docker-compose') {
            agent{ label 'master' }
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh 'docker-compose up -d'
            }
        }
      stage('slave01'){
            agent{ label 'slave1' }
            steps{
                sh 'pwd'
                sh 'ls -la'
            }
      }
  }
  post{
    always {
          sh 'docker-compose down'
          sh 'docker stop $(docker ps -a -q)'
          sh 'docker rm $(docker ps -a -q) -f'
        cleanWs deleteDirs: true, notFailBuild: true
    }
}
}
