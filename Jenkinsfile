pipeline {
    agent any
    stages { 
        stage('build') {
            steps {
                echo 'build'
                sh 'docker build . -t my_clock:1'
                sh 'docker push yuvalshaul/my_clock:1'
            }
        }
        stage('Moshe') {
            when{
                branch "moshe"
            }
            steps {
                echo 'build'
            }
        }
        stage('Deploy'){
            when{
                branch "main"
            }
            steps{
                echo "deploy"
            }
        }
    }
}

