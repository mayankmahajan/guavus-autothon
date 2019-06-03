pipeline {
  agent any
  
  stages {
    
    stage("Build Test"){
        
        stages {
            stage ("Install required Python dependencies"){
                steps {
                        
                        sh "virtualenv venv --python=python2.7 && source venv/bin/activate && pip install -r requirements.txt && deactivate"
                        
                    }
            }

            stage ("Sample Tests") {
                steps {
                        
                        sh "python -m pytest tests/test.py"
                    }
            }
            

        }
    }
  }

}