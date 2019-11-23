import React from 'react'

export class Header extends React.Component {
	constructor() {
		super();
		this.state = {
			value: 'default',
		}

		// document.addEventListener('')
	}

	_onClick() {
		alert('click');
	}

	render() {
		return (
			<div onClick={ this._onClick }>
				Goood
			</div>
		)
	}

}