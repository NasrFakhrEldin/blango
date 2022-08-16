

// class Greeter{
//   constructor(name){
//     this.name = name
//   }

//   getGreeting(){
//     if(this.name === undefined){
//       return 'Hello, no name'
//     }
//     return 'Hello, '+this.name
//   }

//   showGreeting(greetingMessage){
//     console.log(greetingMessage)
//   }

//   greet(){
//     this.showGreeting(this.getGreeting())
//   }
// }

// class DelayedGreeter extends Greeter{
  
//   delay = 2*1000

//   constructor(name, delay){
//     super(name)
//     if(delay !== undefined){
//       this.delay = delay
//     }
//   }

//   greet(){
//     setTimeout(
//       ()=>{
//       this.showGreeting(this.getGreeting())
//     }, this.delay)
//   }
// }

// // const dg2 = new DelayedGreeter('Patchy 2 Seconds')
// // dg2.greet()

// // const dg1 = new DelayedGreeter('Patchy 1 Second', 1000)
// // dg1.greet()


// function resolvedCallback(data){
//   console.log('Resolved with data '+ data)
// }
// function rejectedCallback(message){
//   console.log('Rejected with message '+message)
// }

// const lazyAdd = function(a, b){
//   const doAdd = (resolve, reject)=>{
//     if(typeof a !== 'number' || typeof b !== 'number'){
//       return reject("a and b must be numbers")
//     }else{
//       const sum = a+b
//       return resolve(sum)
//     }
//   }
//   return new Promise(doAdd)
// }

// const p =lazyAdd(3, 4)
// p.then(resolvedCallback, rejectedCallback)

// lazyAdd("n", "a").then(resolvedCallback, rejectedCallback)


class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }

  render () {
    let buttonText

    if (this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.handleClick()
        }
      },
      buttonText
    )
  }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)