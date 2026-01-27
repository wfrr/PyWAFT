pipeline {
    agent {
        label 'linux'
    }

    environment {
        DISPLAY = ":99"
    }

    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Node 1') {
                    agent {
                        label "ubuntu-vm1"
                    }
                    steps {
                        cleanWs()
                        git 'https://github.com/wfrr/PyWAFT.git'
                        sh 'mkdir -p ${WORKSPACE}/config'
                        sh 'curl --output ${WORKSPACE}/config/chrome-latest.toml http://192.168.122.8:8888/config/browser/chrome-latest.toml'
                        sh 'curl --output ${WORKSPACE}/config/test.toml http://192.168.122.8:8888/config/stand/test.toml'
                        sh 'Xvfb ${DISPLAY} -screen 0 1920x1080x24 &'
                        sh '''
                        export CI=true
                        python3 -m venv .venv
                        . ${WORKSPACE}/.venv/bin/activate
                        pip install -r requirements.txt
                        pytest -k ui --variables=${WORKSPACE}/config/chrome-latest.toml --variables=${WORKSPACE}/config/test.toml --alluredir=${WORKSPACE}/allure-results --junitxml=${WORKSPACE}/junit-node1.xml 
                        '''
                    }
                    post {
                        always {
                            stash name: "allure-node1", includes: "allure-results/*"
                            stash name: "junit-node1", includes: "junit-node1.xml"
                        }
                    }
                }
                stage('Node 2') {
                    agent {
                        label "ubuntu-vm2"
                    }
                    steps {
                        cleanWs()
                        git 'https://github.com/wfrr/PyWAFT.git'
                        sh 'mkdir -p ${WORKSPACE}/config'
                        sh 'curl --output ${WORKSPACE}/config/chrome-latest.toml http://192.168.122.8:8888/config/browser/chrome-latest.toml'
                        sh 'curl --output ${WORKSPACE}/config/test.toml http://192.168.122.8:8888/config/stand/test.toml'
                        sh 'Xvfb ${DISPLAY} -screen 0 1920x1080x24 &'
                        sh '''
                        export CI=true
                        python3 -m venv .venv
                        . ${WORKSPACE}/.venv/bin/activate
                        pip install -r requirements.txt
                        pytest -k "not ui" --variables=${WORKSPACE}/config/chrome-latest.toml --variables=${WORKSPACE}/config/test.toml --alluredir=${WORKSPACE}/allure-results --test-group-count 2 --test-group 1 --test-group-by filename --junitxml=${WORKSPACE}/junit-node2.xml 
                        '''
                    }
                    post {
                        always {
                            stash name: "allure-node2", includes: "allure-results/*"
                            stash name: "junit-node2", includes: "junit-node2.xml"
                        }
                    }
                }
                stage('Node 3') {
                    agent {
                        label "windows-vm1"
                    }
                    steps {
                        cleanWs()
                        git 'https://github.com/wfrr/PyWAFT.git'
                        bat 'mkdir %WORKSPACE%\\config'
                        bat 'curl --output %WORKSPACE%\\config\\chrome-latest.toml http://192.168.122.8:8888/config/browser/chrome-latest.toml'
                        bat 'curl --output %WORKSPACE%\\config\\test.toml http://192.168.122.8:8888/config/stand/test.toml'
                        bat '''
                        set CI=true
                        call python -m venv .venv
                        call %WORKSPACE%\\.venv\\Scripts\\activate.bat
                        call pip install -r requirements.txt
                        call pytest -k "not ui" --variables=%WORKSPACE%\\config\\chrome-latest.toml --variables=%WORKSPACE%\\config\\test.toml --alluredir=%WORKSPACE%\\allure-results --test-group-count 2 --test-group 2 --test-group-by filename --junitxml=%WORKSPACE%\\junit-node3.xml 
                        '''
                    }
                    post {
                        always {
                            stash name: "allure-node3", includes: "allure-results/*"
                            stash name: "junit-node3", includes: "junit-node3.xml"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            unstash "allure-node1"
            unstash "allure-node2"
            unstash "allure-node3"
            unstash "junit-node1"
            unstash "junit-node2"
            unstash "junit-node3"
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']],
                   reportBuildPolicy: 'ALWAYS',
                   report: 'allure-report'
            archiveArtifacts artifacts: '**/allure-results/'
            junit testResults: '**/junit*.xml'
            cleanWs cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true
        }
    }
}
