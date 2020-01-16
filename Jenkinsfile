pipeline {
    agent { label 'master'}
    stages {
        /*stage('local docker image') {
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
                sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', passThreshold: 95.0, reportFileName: 'report.html', unstableThreshold: 5.0
            }*/

      stage('slave01 + docker approach'){
            agent{ label 'slave01' }
            steps{
                /*sh "docker network create ${network}"
                sh "docker run -d -p 4444:4444 --name ${seleniumHub} --network ${network} selenium/hub"
                sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${chrome} selenium/node-chrome"
                sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${firefox} selenium/node-firefox"
                */
                sh 'docker-compose -f docker-compose1.yml up -d'
                sleep(time:20,unit:"SECONDS")
                sh 'pwd'
                sh 'ls -la'
                sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', passThreshold: 95.0, reportFileName: 'report.html', unstableThreshold: 5.0
                sh 'docker-compose -f docker-compose1.yml down'
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
