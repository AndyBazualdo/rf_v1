pipeline {
    agent none
    stages {
      /*stage('local docker image') {
            agent { docker { image 'gato756/rf_v1:latest' }
            }
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh "python -m robot.run --NoStatusRC /home/andy/tests/Outlook/test1.robot"
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
              agent{ label 'slave01' }
              steps{
                  sh 'pwd'
                  sh 'ls -la'
                  sh "cd ./tests/Outlook/"
                  sh 'pwd'
                  sh 'ls -la'
                  sh "python -m robot.run --NoStatusRC ./tests/Outlook/test1.robot"
              }
      }*/
      stage('slave01 with plugin'){
            agent{ label 'slave01' }
            steps{
                sh 'pwd'
                sh 'ls -la'
                //sh "python -m robot.run --NoStatusRC ./tests/Outlook/test1.robot"
                sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', reportFileName: 'report.html'
            }
      }
  }
  post{
    always {
        node('master') {
          sh 'docker-compose down'
          //sh 'docker rm $(docker ps -a -q) -f'
          cleanWs deleteDirs: true, notFailBuild: true
        }
      }
    }
}
