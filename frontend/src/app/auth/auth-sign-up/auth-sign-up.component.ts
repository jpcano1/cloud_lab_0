import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl,
  FormGroup, Validators } from '@angular/forms';
import { IUser } from '../../interfaces';
import * as $ from "jquery";

@Component({
  selector: 'app-auth-sign-up',
  templateUrl: './auth-sign-up.component.html',
  styleUrls: ['./auth-sign-up.component.css']
})
export class AuthSignUpComponent implements OnInit {

  credentials = {}

  form: FormGroup;

  isSubmitted: boolean = false;

  userLogged: IUser;

  constructor(private formBuilder: FormBuilder) {
    this.form = this.formBuilder.group({
      email: new FormControl('', [
        Validators.required,
        Validators.pattern(/^([\w\-\.]+)@((\[([0-9]{1,3}\.){3}[0-9]{1,3}\])|(([\w\-]+\.)+)([a-zA-Z]{2,4}))$/)
      ]),
      password: new FormControl('', [
        Validators.required,
        // Validators.pattern(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])*.{8,10}$/)
      ]),
      password_confirmation: new FormControl('', [
        Validators.required
      ]),
    });
  }

  emailValidation() {
    return (this.form.get('email').errors && this.isSubmitted) ||
      (this.form.get('email').errors && this.form.get('email').touched);
  }

  emailValid() {
    return !this.form.get('email').errors && this.form.get('email').touched;
  }

  passwordValidation() {
    return (this.form.get('password').errors && this.isSubmitted) ||
      (this.form.get('password').errors && this.form.get('password').touched);
  }

  passwordValid() {
    return !this.form.get('password').errors && this.form.get('password').touched
  }

  showPassword()
  {
    let password = $('#pass'),
      toggle = $('#show-password');

    toggle.click(function()
    {
      toggle.is(':checked') ? password.attr('type', 'text'):password.attr('type', 'password');
    });
  }

  ngOnInit(): void {
    this.showPassword();
  }
}
