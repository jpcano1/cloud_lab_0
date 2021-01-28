import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {

  constructor(private auth: AuthService,
              private router: Router) { }

  ngOnInit(): void {
  }

  logout() {
    this.auth.logout();
    this.router.navigateByUrl("/users/login")
      .then(result => console.log(result))
      .catch(error => console.log(error));
    alert("You've been logged out");
  }
}
