pipeline {
    agent any
    stages { 
        stage('build') {
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

