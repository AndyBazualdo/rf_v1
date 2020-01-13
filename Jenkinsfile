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
                wrap([$class: 'Xvfb', additionalOptions: '', assignedLabels: '', debug: true, displayNameOffset: 0, screen: '']) {
                  sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                }
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', passThreshold: 95.0, reportFileName: 'report.html', unstableThreshold: 5.0
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
