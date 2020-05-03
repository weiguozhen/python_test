node(){
    stage('构建'){
        //把代码从git上面clone下来
        checkout scm
    }
    stage('部署'){
        //执行运行脚本 run.sh
        sh 'python3 auto_deploy2.py'
    }
    stage('测试'){
        //test
	sh 'robot -P . tc'
    }
    stage('交付'){
        //delivery
    }
}
