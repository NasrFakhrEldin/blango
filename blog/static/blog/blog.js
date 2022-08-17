
/*
class Greeter{
  constructor(name){
    this.name = name
  }

  getGreeting(){
    if(this.name === undefined){
      return 'Hello, no name'
    }
    return 'Hello, '+this.name
  }

  showGreeting(greetingMessage){
    console.log(greetingMessage)
  }

  greet(){
    this.showGreeting(this.getGreeting())
  }
}

class DelayedGreeter extends Greeter{
  
  delay = 2*1000

  constructor(name, delay){
    super(name)
    if(delay !== undefined){
      this.delay = delay
    }
  }

  greet(){
    setTimeout(
      ()=>{
      this.showGreeting(this.getGreeting())
    }, this.delay)
  }
}

const dg2 = new DelayedGreeter('Patchy 2 Seconds')
dg2.greet()

const dg1 = new DelayedGreeter('Patchy 1 Second', 1000)
dg1.greet()


function resolvedCallback(data){
  console.log('Resolved with data '+ data)
}
function rejectedCallback(message){
  console.log('Rejected with message '+message)
}

const lazyAdd = function(a, b){
  const doAdd = (resolve, reject)=>{
    if(typeof a !== 'number' || typeof b !== 'number'){
      return reject("a and b must be numbers")
    }else{
      const sum = a+b
      return resolve(sum)
    }
  }
  return new Promise(doAdd)
}

const p =lazyAdd(3, 4)
p.then(resolvedCallback, rejectedCallback)

lazyAdd("n", "a").then(resolvedCallback, rejectedCallback)


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

  render () {
    let buttonText

    if (this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return <button
      className="btn btn-primary mt-2"
      onClick={
        () => {
          this.handleClick()
        }
      }
    >
      {buttonText}
    </button>
  }

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)


class PostRow extends React.Component {
  render () {
    const post = this.props.post

    let thumbnail

    if (post.hero_image.thumbnail) {
      thumbnail = <img src={post.hero_image.thumbnail}/>
    } else {
      thumbnail = '-'
    }

    return <tr>
      <td>{post.title}</td>
      <td>
        {thumbnail}
      </td>
      <td>{post.tags.join(', ')}</td>
      <td>{post.slug}</td>
      <td>{post.summary}</td>
      <td><a href={'/post/' + post.slug + '/'}>View</a></td>
    </tr>
  }
}

class PostTable extends React.Component {
  state = {
    dataLoaded: true,
    data: {
      results: [
        {
          id: 15,
          tags: [
            'django', 'react'
          ],
          'hero_image': {
            'thumbnail': 'https://miraclepromise-antennacarmen-8000.codio.io/media/__sized__/hero_images/carbon-thumbnail-100x100.png',
            'full_size': 'https://miraclepromise-antennacarmen-8000.codio.io/media/hero_images/carbon.png'
          },
          title: 'Test Post',
          slug: 'test-post',
          summary: 'A test post, created for Django/React.'
        }
      ]
    }
  }

  render () {
    let rows
    if (this.state.dataLoaded) {
      if (this.state.data.results.length) {
        rows = this.state.data.results.map(post => <PostRow post={post} key={post.id}/>)
      } else {
        rows = <tr>
          <td colSpan="6">No results found.</td>
        </tr>
      }
    } else {
      rows = <tr>
        <td colSpan="6">Loading&hellip;</td>
      </tr>
    }

    return <table className="table table-striped table-bordered mt-2">
      <thead>
      <tr>
        <th>Title</th>
        <th>Image</th>
        <th>Tags</th>
        <th>Slug</th>
        <th>Summary</th>
        <th>Link</th>
      </tr>
      </thead>
      <tbody>
      {rows}
      </tbody>
    </table>
  }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(PostTable),
  domContainer
)

/*
['/api/v1/posts/', '/', '/abadurl/'].forEach(url => {
  fetch(url).then(response => {
    if (response.status !== 200) {
      throw new Error('Invalid status from server: ' + response.statusText)
    }

    return response.json()
  }).then(data => {
    // do something with data, for example
    console.log(data)
  }).catch(e => {
    console.error(e)
  })
})
*/

class PostRow extends React.Component {
  render () {
    const post = this.props.post

    let thumbnail

    if (post.hero_image.thumbnail) {
      thumbnail = <img src={post.hero_image.thumbnail}/>
    } else {
      thumbnail = '-'
    }

    return <tr>
      <td>{post.title}</td>
      <td>
        {thumbnail}
      </td>
      <td>{post.tags.join(', ')}</td>
      <td>{post.slug}</td>
      <td>{post.summary}</td>
      <td><a href={'/post/' + post.slug + '/'}>View</a></td>
    </tr>
  }
}

class PostTable extends React.Component {
  state = {
    dataLoaded: false,
    data: null
  }

  render () {
    let rows
    if (this.state.dataLoaded) {
      if (this.state.data.results.length) {
        rows = this.state.data.results.map(post => <PostRow post={post} key={post.id}/>)
      } else {
        rows = <tr>
          <td colSpan="6">No results found.</td>
        </tr>
      }
    } else {
      rows = <tr>
        <td colSpan="6">Loading&hellip;</td>
      </tr>
    }

    return <table className="table table-striped table-bordered mt-2">
      <thead>
      <tr>
        <th>Title</th>
        <th>Image</th>
        <th>Tags</th>
        <th>Slug</th>
        <th>Summary</th>
        <th>Link</th>
      </tr>
      </thead>
      <tbody>
      {rows}
      </tbody>
    </table>
  }

/*
class ChildButton extends React.Component {
  render () {
    return <button onClick={ () => { this.props.parentCallback('foo') } }>Click Me</button>
  }
}

class ParentContainer extends React.Component {
  aCallback(val) {
    // will log 'foo' when child is clicked
    console.log(val)
  }

  render () {
    return <div>
      <ChildButton parentCallback={ (arg) => { this.aCallback(arg) } } />
    </div>
  }
}
*/

  componentDidMount(){
    fetch(this.props.url).then(response =>{
      if(response.status !== 200){
        throw new Error('Invalid status from server: '+response.statusText)
      }

      return response.json()
    }).then(data =>{
      this.setState({
        dataLoaded: true,
        data:data
      })
    }).catch(e=> {
      console.error(e)
      this.setState({
        dataLoaded: true,
        data:{results:[]}
      })
    })
  }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(
    PostTable,
    {url: postListUrl}
  ),
  domContainer
)


// https://reactjs.org/docs/react-component.html#rarely-used-lifecycle-methods
