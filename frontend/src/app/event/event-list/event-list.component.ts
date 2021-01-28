import { Component, OnInit } from '@angular/core';
import { EventService } from '../event.service';

@Component({
  selector: 'app-event-list',
  templateUrl: './event-list.component.html',
  styleUrls: ['./event-list.component.css']
})
export class EventListComponent implements OnInit {

  events = new Array<object>();
  constructor(private eventService: EventService) { }

  getEvents() {
    this.eventService.getEvents()
      .subscribe(events => {
        this.events = events["events"];
      });
  }

  deleteEvent(index) {
    this.eventService.deleteEvent(this.events[index]["id"])
      .subscribe(response => {
        alert("Deleted event: " + this.events[index]["id"]);
        this.ngOnInit();
      }, error => console.log(error));
  }

  ngOnInit(): void {
    this.getEvents();
  }

}
