pipeline {
    agent any
    stages { 
        stage('build') {
            steps {
                echo 'build'
		sh 'echo Build number is: $BUILD_NUMBER.'
                sh 'docker build . -t yuvalshaul/my_clock:1'
		sh 'docker login'
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

