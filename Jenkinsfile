pipeline {
    agent any
    stages { 
        stage('one: all branches') {
            steps {
                echo 'Hello World'
            }
        }
        stage('two: only fix-*') {
            when {
                branch 'fix-1'
            }
            steps {
                echo 'fix fix'
            }
        }

    }
}
