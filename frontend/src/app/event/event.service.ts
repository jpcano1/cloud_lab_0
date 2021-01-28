import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  constructor(private http: HttpClient,
              private cookie: CookieService) {
  }

  createEvents(event) {
    let headers = new HttpHeaders().set("Authorization", `Bearer ${this.cookie.get("token")}`);
    return this.http.post("/api/events", event, { headers });
  }

  getEvents(): Observable<Array<object>> {
    let headers = new HttpHeaders().set("Authorization", `Bearer ${this.cookie.get("token")}`);
    return this.http.get<Array<object>>("/api/events", { headers });
  }

  getEventDetail(id) {
    let headers = new HttpHeaders().set("Authorization", `Bearer ${this.cookie.get("token")}`);
    return this.http.get("/api/events/" + id, { headers })
  }

  editEvent(id) {

  }

  deleteEvent(id) {
    let headers = new HttpHeaders().set("Authorization", `Bearer ${this.cookie.get("token")}`);
    return this.http.delete("/api/events/" + id, { headers });
  }
}
