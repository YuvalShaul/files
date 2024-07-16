pipeline {
    agent any
    stages { 
        stage('build') {
            steps {
                echo 'build'
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

