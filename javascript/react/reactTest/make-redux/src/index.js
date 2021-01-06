//reducer仅仅用于初始化和计算心的state
function createStore(reducer) {
	let state = null
	const listeners = []
	const subscribe = (listener) => listeners.push(listener)
	const getState = () => state
	const dispatch = (action) => {
		state = reducer(state, action)
		listeners.forEach( (listener) => listener() )
	} 
	dispatch({})
	return { getState, dispatch, subscribe}
}



function renderApp(newAppState, oldAppState={}) {
	if(newAppState === oldAppState) return
	console.log('render app...')
	renderTitle(newAppState.title , oldAppState.title)
	renderContent(newAppState.content, oldAppState.content)
}

function renderTitle(newTitle, oldTitle={}) {
	if(newTitle === oldTitle) return
	console.log('render title...')
	const titleDOM = document.getElementById("title")
	titleDOM.innerHTML = newTitle.text
	titleDOM.style.color = newTitle.color
}

function renderContent(newContent, oldContent={}) {
	if(newContent === oldContent) return
	console.log('render content...')
	const contentDOM = document.getElementById("content")
	contentDOM.innerHTML = newContent.text
	contentDOM.style.color = newContent.color
}


//定一个reducer
function reducer(state, action) {
	if (!state) {
		return {
			title : {
				text : 'React.js 小书',
				color : 'red'
			},
			content: {
				text : 'React.js 小书内容',
				color : 'blue'
			}
		}
	}

	switch (action.type) {
		case 'UPDATE_TITLE_TEXT':
			return {
				...state,
				title : {
					...state.title,
					text : action.text
				}
			}
		case 'UPDATE_TITLE_COLOR':
			return {
				...state,
				title : {
					...state.title,
					color : action.color
				}
			}
		default:
			return state
	}
}

//生成store
const store = createStore(reducer)

//监听数据变化重新渲染页面
store.subscribe( () => {
	renderApp(store.getState())
} )

//首次渲染页面
renderApp(store.getState())

//
store.dispatch({
	type: 'UPDATE_TITLE_TEXT', text: '《React.js 小书》'
})
store.dispatch({ 
	type: 'UPDATE_TITLE_COLOR', color: 'green' 
}) 
