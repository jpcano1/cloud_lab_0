import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import {AuthSignUpComponent} from '../auth/auth-sign-up/auth-sign-up.component';
import {AuthLoginComponent} from '../auth/auth-login/auth-login.component';

const routes: Routes = [
  {
    path: "users",
    children: [
      {
        path: "signup",
        component: AuthSignUpComponent
      },
      {
        path: "login",
        component: AuthLoginComponent
      }
    ]
  },
  {
    path: "",
    component: AuthLoginComponent
  }
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes, {
      onSameUrlNavigation: "reload"
    })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
