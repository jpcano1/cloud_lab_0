import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthLoginComponent } from './auth-login/auth-login.component';
import { AuthSignUpComponent } from './auth-sign-up/auth-sign-up.component';



@NgModule({
  declarations: [AuthLoginComponent, AuthSignUpComponent],
  imports: [
    CommonModule
  ]
})
export class AuthModule { }
