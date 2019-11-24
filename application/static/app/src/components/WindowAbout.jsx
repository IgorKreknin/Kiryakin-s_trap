import React from 'react'
import styles from '../styles/window_about.module.css'

export class WindowAbout extends React.Component {
	render() {
		return (
			<div className={ styles.container }>
				<img src={ '' } alt="Photo" className={styles.photo} />
			</div>
		)
	}
}