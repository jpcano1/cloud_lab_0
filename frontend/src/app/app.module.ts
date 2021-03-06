import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';
import { AppRoutingModule } from './app-routing/app-routing.module';
import { NavigationComponent } from './navigation/navigation.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { ModalDialogModule } from 'ngx-modal-dialog';
import { NgxPermissionsModule } from 'ngx-permissions';
import { EventModule } from './event/event.module';

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AuthModule,
    EventModule,
    AppRoutingModule,
    ReactiveFormsModule,
    ModalDialogModule.forRoot(),
    NgxPermissionsModule.forRoot()
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
