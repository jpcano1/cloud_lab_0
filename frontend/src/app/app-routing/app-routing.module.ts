import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { AuthSignUpComponent } from '../auth/auth-sign-up/auth-sign-up.component';
import { AuthLoginComponent } from '../auth/auth-login/auth-login.component';
import { EventListComponent } from '../event/event-list/event-list.component';
import { NgxPermissionsGuard } from 'ngx-permissions';

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
    ],
    canActivate: [NgxPermissionsGuard]
  },
  {
    path: "",
    component: EventListComponent
  },
  {
    path: "event",
    children: [
      {
        path: "",
        component: EventListComponent
      }
    ]
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
