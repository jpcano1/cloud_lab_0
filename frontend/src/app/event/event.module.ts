import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EventListComponent } from './event-list/event-list.component';
import { EventDetailComponent } from './event-detail/event-detail.component';
import { EventCreateComponent } from './event-create/event-create.component';
import { EventUpdateComponent } from './event-update/event-update.component';
import { ReactiveFormsModule } from '@angular/forms';
import { EventService } from './event.service';
import { HttpClientModule } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    EventListComponent,
    EventDetailComponent,
    EventCreateComponent,
    EventUpdateComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule
  ],
  providers: [EventService, CookieService]
})
export class EventModule { }
