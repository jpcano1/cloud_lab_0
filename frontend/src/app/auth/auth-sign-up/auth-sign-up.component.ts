import {Component, OnInit, ViewContainerRef} from '@angular/core';
import { FormBuilder, FormControl,
  FormGroup, Validators } from '@angular/forms';
import { IUser } from '../../interfaces';
import * as $ from "jquery";
import { AuthService } from '../auth.service';
import { ModalDialogService, SimpleModalComponent } from 'ngx-modal-dialog';

@Component({
  selector: 'app-auth-sign-up',
  templateUrl: './auth-sign-up.component.html',
  styleUrls: ['./auth-sign-up.component.css']
})
export class AuthSignUpComponent implements OnInit {

  form: FormGroup;

  isSubmitted: boolean = false;

  constructor(private formBuilder: FormBuilder,
              private auth: AuthService) {
    this.form = this.formBuilder.group({
      email: new FormControl('', [
        Validators.required,
        Validators.pattern(/^([\w\-\.]+)@((\[([0-9]{1,3}\.){3}[0-9]{1,3}\])|(([\w\-]+\.)+)([a-zA-Z]{2,4}))$/)
      ]),
      password: new FormControl('', [
        Validators.required,
        // Validators.pattern(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])*.{3,10}$/)
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

  showPassword()
  {
    let password = $('#pass'),
      toggle = $('#show-password');

    toggle.click(function() {
      toggle.is(':checked') ? password.attr('type', 'text'):password.attr('type', 'password');
    });
  }

  onLoginSubmit() {
    this.isSubmitted = true;

    let user: IUser = this.form.value;

    if (this.form.valid) {
      this.auth.signup(user)
        .subscribe(response =>  alert(response.message + "\nPlease Log In"),
            error => alert(error.error.error_message)
        );
    }
  }

  ngOnInit(): void {
    this.showPassword();
  }
}
