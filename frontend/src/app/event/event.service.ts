import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

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

  getEvents() {
    let headers = new HttpHeaders().set("Authorization", `Bearer ${this.cookie.get("token")}`);
    return this.http.get("/api/events", {headers});
  }

  getEventDetail(id) {

  }

  editEvent(id) {

  }

  deleteEvent(id) {

  }
}
