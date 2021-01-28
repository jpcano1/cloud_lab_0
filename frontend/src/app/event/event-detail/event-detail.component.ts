import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {EventService} from '../event.service';

@Component({
  selector: 'app-event-detail',
  templateUrl: './event-detail.component.html',
  styleUrls: ['./event-detail.component.css']
})
export class EventDetailComponent implements OnInit {

  id: number;

  event: any = {};

  constructor(private route: ActivatedRoute,
              private eventService: EventService) { }

  getEvent() {
    this.eventService.getEventDetail(this.id)
      .subscribe(response => {
        this.event = response["event"];
      });
  }

  ngOnInit(): void {
    this.id = + this.route.snapshot.paramMap.get("id");
    this.getEvent();
  }
}
