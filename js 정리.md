// const elem1 = document.querySelector('#title-1')
// // console.log(elem1)

// const elem2 = document.querySelector('#list-1')
// // console.log(elem2)

// const elemList = document.querySelectorAll('li')
// // NodeList의 형태로 나옴 => 유사배열
// // querySelectorAll에 넣으면 요소 수에 상관없이 항상 NodeList의 형태로 반환

const elem1 = document.querySelector('#list-1')
// const myHtml = elem1.innerHTML
// elem1.innerHTML += '<li>빨간색 아이폰 갖고싶다</li>'
// const myHtml = elem1.outerHTML
// console.log(myHtml)

// 1. firstElementChild
const firstElem = elem1.firstElementChild
console.log(firstElem)

// 2. children
const children = elem1.children
console.log(children[0])

// 3. lastElementChild
const lastElem = elem1.lastElementChild
console.log(lastElem)

// 내가 선택한 노드의 형제 노드 (앞에 있는)
const previous = elem1.previousElementSibling
console.log(previous)

// 내가 선택한 노드의 형제 노드 (뒤에 있는)
const next = elem1.nextElementSibling
console.log(next)


const elem2 = document.querySelector('#title-1')

const myText1 = elem1.innerHTML
console.log(myText1)

const myText2 = elem1.textContent
console.log(myText2)

elem1.remove()



#이동시키기(append 사용하기)

#class 여러개 쓰기 (classlist)

#class toggle (있으면없게 없으면있게)

function myclick(e){

​	console.log(e.target)}   (객체가 반환된다)



#이벤트 버블링을 조심해야 한다



브라우저, 돔트리

파싱 x

ecma x

세미콜론 x

스타일 가이드 x

변수의 차이점 

데이터 타입 

typeof 다르게 나오는거?

일급객체

arrow function

키는 문자열만 가능

구조분해할당

js 만든사람



