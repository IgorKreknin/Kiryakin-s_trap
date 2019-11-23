import React from 'react'
import styles from '../styles/auth_modal.module.css'

export class Auth extends React.Component {
	constructor() {
		super();
		this.state = {
			value: "auth",
		}
	}

	render() {
		return (
			<div className = { styles.auth_modal_window }>
				<div className = { styles.input_container }>
				</div>
				<div className = { styles.input_container }>
				</div>
			</div>
		)
	}
}