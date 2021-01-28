import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IUser } from '../interfaces';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(data: IUser): Observable<any> {
    return this.http.post("/api/auth/login", data);
  }

  signup(data: object): Observable<any> {
    return this.http.post("/api/auth/signup", data);
  }
}
