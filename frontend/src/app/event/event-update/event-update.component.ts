import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { EventService } from '../event.service';
import * as $ from "jquery";
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-event-update',
  templateUrl: './event-update.component.html',
  styleUrls: ['./event-update.component.css']
})
export class EventUpdateComponent implements OnInit {

  eventForm: FormGroup;

  isSubmitted: boolean = false;

  event: any = {};

  id: number;

  categories: Array<string> = ["conference", "congress", "seminar", "course"]

  constructor(private formBuilder: FormBuilder,
              private route: ActivatedRoute,
              private eventService: EventService) {
    this.eventForm = formBuilder.group({
      name: new FormControl("", [
        Validators.required
      ]),
      begin_date: new FormControl("", [
        Validators.required,
        Validators.pattern(/((\d{2})|(\d))\/((\d{2})|(\d))\/((\d{4})|(\d{2}))/)
      ]),
      end_date: new FormControl("", [
        Validators.required,
        Validators.pattern(/((\d{2})|(\d))\/((\d{2})|(\d))\/((\d{4})|(\d{2}))/)
      ]),
      address: new FormControl("", [
        Validators.required
      ])
    })
  }

  validateField(field: string) {
    return (this.eventForm.get(field).errors && this.isSubmitted) ||
      (this.eventForm.get(field).errors && this.eventForm.get(field).touched);
  }

  getEvent() {
    this.eventService.getEventDetail(this.id)
      .subscribe(response => {
        this.event = response["event"];
      });
  }

  submitForm() {
    this.isSubmitted = true;

    let virtual = $("#virtual").is(":checked");
    let formCheck = $(".cat");
    let category = "";
    for (let i = 0; i < formCheck.length; i++) {
      if (formCheck[i].checked) {
        category = this.categories[i];
      }
    }
    let formValue = {
      "category": category,
      "virtual": virtual,
      ...this.eventForm.value
    }

    if (formValue.name == "") {
      formValue.name = this.event.name;
    } if (formValue.begin_date == "") {
      formValue.begin_date = this.event.begin_date;
    } if (formValue.end_date == "") {
      formValue.end_date = this.event.end_date;
    } if (formValue.address == "") {
      formValue.address = this.event.address;
    }

    this.eventService.editEvent(this.id, formValue)
      .subscribe(response => {
        alert("Event Updated")
      }, error => {
        if (error.error.error_message) {
          alert(error.error.error_message);
        } else if (error.error.msg) {
          alert(error.error.msg);
        }
      });
  }

  ngOnInit(): void {
    this.id = + this.route.snapshot.paramMap.get("id");
    this.getEvent();
  }
}
