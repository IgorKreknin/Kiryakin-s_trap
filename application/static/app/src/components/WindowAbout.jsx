import React from 'react'
import styles from '../styles/window_about.module.css'

export class WindowAbout extends React.Component {
	constructor() {
		super();
		this.state ={
			value: "",
		}

		this._onClick = this._onClick.bind(this);
	}

	_onClick() {
		document.dispatchEvent(new Event('printAll'));
		console.log('qweqwe');
	}

	render() {
		return (
			<div>
			<div className={ styles.container }>
				<img src={ '' } alt="Photo" className={styles.photo} />
			</div>
			<div className={ styles.showAll } onClick={ this._onClick }>Back</div>
			</div>
		)
	}
}
