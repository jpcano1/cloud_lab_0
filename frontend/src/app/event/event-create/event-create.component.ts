import { Component, OnInit } from '@angular/core';
import {FormArray, FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import * as $ from "jquery";
import {EventService} from '../event.service';

@Component({
  selector: 'app-event-create',
  templateUrl: './event-create.component.html',
  styleUrls: ['./event-create.component.css']
})
export class EventCreateComponent implements OnInit {

  eventForm: FormGroup;

  isSubmitted: boolean = false;

  categories: Array<string> = ["conference", "congress", "seminar", "course"]

  checkboxGroup: FormGroup;

  constructor(private formBuilder: FormBuilder,
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

    this.checkboxGroup = formBuilder.group({
      myValues: this.addValuesControls()
    })
  }

  validateField(field: string) {
    return (this.eventForm.get(field).errors && this.isSubmitted) ||
      (this.eventForm.get(field).errors && this.eventForm.get(field).touched);
  }

  addValuesControls() {
    let arr = this.categories.map(category => {
      if (category == "conference") {
        return this.formBuilder.control(true);
      } else {
        return this.formBuilder.control(false);
      }
    });
    return this.formBuilder.array(arr);
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

    if (this.eventForm.valid) {
      this.eventService.createEvents(formValue)
        .subscribe(response => {
          alert("Event Created")
        }, error => {
          if (error.error.error_message) {
            alert(error.error.error_message);
          } else if (error.error.msg) {
            alert(error.error.msg);
          }
        });
    }
  }

  get valuesArray() {
    return <FormArray> this.checkboxGroup.get("myValues");
  }

  selectedCategory() {
    let category = "";
    this.valuesArray.controls.forEach((control, i) => {
    });
    return category;
  }

  ngOnInit(): void {
  }

}
