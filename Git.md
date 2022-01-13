# Git

1. 분산 버전 관리 시스템
   * 코드의 히스토리를 관리하는 도구
   * 개발되어온 과정 파악 가능
   * 이전 버전과의 변경 사항 비교 및 분석
   
2. 깃 vs 깃허브
   - 깃은 분산 버전 관리 시스템
   - 깃허브는 깃의 저장소 서비스이다
   
   
   
   # linux 명령어
   
   
   
   
   
   * CLI는 명령프롬프트(unix, linux명령어가 사용되지 않음) 환경을 말한다. GUI는 그래픽 환경(버튼) / powershell에서 일부 기능 구현(dir=ls)
   
   - 현재 위치의 폴더, 파일 목록보기 ls
   
   - 현재 위치 이동하기 cd\<path> //    cd ..(상위 폴더로 이동)
   
   - mkdir name 디렉토리 생성
   
   -  tap 자동완성
   
   - touch 파일 생성
   
   - ~ 물결표시는 홈 디렉토리를 말해준다
   
   - rm name 은  파일 삭제
   
   - rm -r name은 폴더 삭제
   
   - code . 을 입력하면 vs code 실행됨
   
     

#  Git 기본기

* Repository :  git inti 명령어로 로컬 저장소를 생성함
* 특정 버전으로 남긴다 => 커밋한다
* 커밋 : working directory(내가 작업하는 실제 디렉), staging area(특정 버전으로 관리 파일), repository(커밋들의 저장//.git)
* untracked (git add)추적되지 않은 모든 파일과 수정된 파일 모두를 staging area에 올리게 된다-> tracked (git commit) -> commit01 -> modified
* git status 깃의 상태를 보여줌 / git add(띄고). 를 치면 모든걸 수정할 수 있음 cf).은 현재위치를 말함
* 레포지토리 안에 레포지토리를 만들면 안됨
* 타이핑이안되면 q를 누르자
* git init -> git config user.name -> git add "" -> git commit -m ""
* staging area가 필요한 이유 : 파일들의 진척 속도가 다르기 때문
* git diff commit4자리 commit4자리 : 두 커밋의 비교를 보임
* github에 있는거 가져오기 : git clone http://~
* git push origin master 후 비밀번호 입력해야함
* git pull(바뀐것만 가져오기)
* 대탈출 방법 : shift +: q
* local에서 remote로 repo 올리기 : git remote add **origin** http:// , git push -u origin master