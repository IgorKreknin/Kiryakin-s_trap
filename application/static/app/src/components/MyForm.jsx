import React from 'react'
import styles from '../styles/auth_modal.module.css'
import userIcon from '../img/userIcon.svg'
import nameIcon from '../img/nameIcon.svg'
import keyIcon from '../img/key.svg'
import lampIcon from '../img/lamp.svg'
import addIcon from '../img/add.svg'

export class MyForm extends React.Component {
	constructor() {
		super();
		this.state = {
			login: "",
			password: "",
			password_repeat: "",
			name: "",
			lastname: "",
			phone: "",
			email: "",
			type: "register",
			registerStyles: styles.login_fields,
			loginStyles: styles.login_fields,
			iconStyles: styles.hide,
			placeholder: "РЕГИСТРАЦИЯ",
		}

		this._onChangeName = this._onChangeName.bind(this);
		this._onChangeLastname = this._onChangeLastname.bind(this);
		this._onChangePhone = this._onChangePhone.bind(this);
		this._onChangeLogin = this._onChangeLogin.bind(this);
		this._onChangeEmail = this._onChangeEmail.bind(this);
		this._onChangePassword = this._onChangePassword.bind(this);
		this._onChangePasswordRepeat = this._onChangePasswordRepeat.bind(this);
		this._onSubmit = this._onSubmit.bind(this);
		this._onClickChange = this._onClickChange.bind(this)
	}

	_onSubmit(e) {
  		e.preventDefault();
  		let st = this.state;

  		let result = {
  			name: st.name,
  			lastname: st.lastname,
  			phone: st.phone,
  			login: st.login,
  			email: st.email,
  			password: st.password,
  			password_repeat: st.password_repeat,
  			action: this.state.type,
  		}

  		this.setState({
			login: "",
			password: "",
			password_repeat: "",
			name: "",
			lastname: "",
			phone: "",
			email: "",
			type: this.state.type,
			registerStyles: this.state.registerStyles,
			placeholder: this.state.placeholder,
		});

		console.log(result);
		let xhr = new XMLHttpRequest();
		xhr.open('GET', 'http://127.0.0.1:8000/test', true);
		xhr.send(result);
  	}

	_onChangeName(event){
		this.setState({name: event.target.value});
	}

	_onChangeLastname(event){
		this.setState({lastname: event.target.value});
	}

	_onChangePhone(event){
		this.setState({phone: event.target.value});
	}

	_onChangeLogin(event){
		this.setState({login: event.target.value});
	}

	_onChangeEmail(event){
		this.setState({email: event.target.value});
	}

	_onChangePassword(event){
		this.setState({password: event.target.value});
	}

	_onChangePasswordRepeat(event){
		this.setState({password_repeat: event.target.value});
	}

	_onClickChange(){
		let st = this.state;
		if (st.type == "auth"){
			st.type = "register";
			st.placeholder = "РЕГИСТРАЦИЯ";
			st.registerStyles = styles.login_fields;
			st.iconStyles = styles.hide;
		}else{
			st.type = "auth";
			st.placeholder = "ВХОД"
			st.registerStyles = styles.hide;
			st.iconStyles = styles.login_image;
		}

		this.setState(st);
	}

	render() {
		return(
			<div className = { styles.auth_modal_window }>
				<img src={ userIcon } alt="" className={ styles.user_icon } />
				<form onSubmit={this._onSubmit} className = { styles.auth_form }>
					<div className={ this.state.registerStyles }>
						<input type="text" name="name" placeholder="Имя" value={this.state.name} onChange={this._onChangeName} />
					</div>
					<div className={ this.state.registerStyles }>
						<input type="text" name="lastname" placeholder="Фамилия" value={this.state.lastname} onChange={this._onChangeLastname} />
					</div>
					<div className={ this.state.registerStyles }>
						<input type="text" name="phone" placeholder="Телефон" value={this.state.phone} onChange={this._onChangePhone}  />
					</div>
					<div className={ this.state.loginStyles }>
						<img src={ nameIcon } alt="" className={ this.state.iconStyles } />
						<input type="text" name="message" placeholder="Логин" value={this.state.login} onChange={this._onChangeLogin}  />
					</div>
					<div className={ this.state.registerStyles }>
						<input type="text" name="message" placeholder="Почта" value={this.state.email} onChange={this._onChangeEmail}  />
					</div>
					<div className={ this.state.loginStyles }>
						<img src={ keyIcon } alt="" className={ this.state.iconStyles } />
						<input type="text" name="message" placeholder="Пароль" value={this.state.password} onChange={this._onChangePassword}  />
						<img src={ lampIcon } alt="" className={ this.state.iconStyles } />
					</div>
					<div className={ this.state.registerStyles }>
						<input type="text" name="message" placeholder="Повторите пароль" value={this.state.password_repeat} onChange={this._onChangePasswordRepeat} />
					</div>
					<div style={{height: '40px'}}>
						<input type="submit" name="send" value={ this.state.placeholder } className={ styles.send_button }/>
						<img src={ addIcon } className={ styles.add_icon } onClick = { this._onClickChange } alt=""/>
					</div>
				</form>
			</div>
		)
	}
}
