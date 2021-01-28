import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IUser } from '../interfaces';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import {NgxPermissionsService, NgxRolesService} from 'ngx-permissions';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient,
              private cookie: CookieService,
              private router: Router,
              private rolesService: NgxRolesService,
              private permissionsService: NgxPermissionsService) { }

  start() {
    this.permissionsService.flushPermissions();
    this.rolesService.flushRoles();

    let token = this.cookie.get("token");
    let role = localStorage.getItem("role");

    if (!token) {
      this.setRole("GUEST");
    } else if (!role) {
      this.logout();
    } else {
      this.setRole("USER");
    }
  }

  setRole(role) {
    this.rolesService.flushRoles();
    this.rolesService.addRole(role, [""]);
  }

  logout() {
    this.cookie.delete("token");
    this.cookie.delete("password");
    this.setRole("GUEST");
    this.router.navigateByUrl("/")
      .then(result => console.log(result))
      .catch(error => console.log(error));
    localStorage.removeItem("role");
  }

  login(data: IUser): Observable<any> {
    return this.http.post("/api/auth/login", data);
  }

  signup(data: IUser): Observable<any> {
    return this.http.post("/api/auth/signup", data);
  }
}
