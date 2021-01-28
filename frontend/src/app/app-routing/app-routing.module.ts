import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { AuthSignUpComponent } from '../auth/auth-sign-up/auth-sign-up.component';
import { AuthLoginComponent } from '../auth/auth-login/auth-login.component';
import { EventListComponent } from '../event/event-list/event-list.component';
import { NgxPermissionsGuard } from 'ngx-permissions';
import { EventCreateComponent } from '../event/event-create/event-create.component';
import { EventDetailComponent } from '../event/event-detail/event-detail.component';

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
    canActivate: [NgxPermissionsGuard],
    data: {
      permissions: {
        only: ["GUEST"]
      }
    },
  },
  {
    path: "",
    component: EventListComponent,
    canActivate: [NgxPermissionsGuard],
    data: {
      permissions: {
        only: ["USER"]
      }
    },
  },
  {
    path: "event",
    children: [
      {
        path: "",
        component: EventListComponent
      },
      {
        path: "create",
        component: EventCreateComponent
      },
      {
        path: ":id",
        component: EventDetailComponent
      }
    ],
    canActivate: [NgxPermissionsGuard],
    data: {
      permissions: {
        only: ["USER"]
      }
    },
  },
  {
    path: "*",
    redirectTo: ""
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
