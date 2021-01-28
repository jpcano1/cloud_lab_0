import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import * as $ from "jquery";
import {IUser} from '../../interfaces';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-auth-login',
  templateUrl: './auth-login.component.html',
  styleUrls: ['./auth-login.component.css']
})
export class AuthLoginComponent implements OnInit {

  form: FormGroup;

  isSubmitted: boolean = false;

  constructor(private formBuilder: FormBuilder,
              private auth: AuthService,
              private cookie: CookieService) {
    let password = this.cookie.get("password");
    this.form = this.formBuilder.group({
      email: new FormControl('juan@hotmail.com', [
        Validators.required,
      ]),
      password: new FormControl( password? password: 'hola', [
        Validators.required,
      ])
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

  onLoginSubmit() {
    this.isSubmitted = true;

    let user: IUser = this.form.value;

    if (this.form.valid) {
      this.auth.login(user)
        .subscribe(response => {
          let toggle = $('#save-password');
          if (toggle.is(":checked")) {
            let password = this.form.get("password").value;
            this.cookie.set("password", password);
          }
          this.cookie.set("token", response.access_token);
          localStorage.setItem("role", "USER");
          this.auth.setRole("USER");
          alert(response.message);
        }, error => alert(error.error.error_message)
        );
    }
  }

  ngOnInit(): void {
  }

}
