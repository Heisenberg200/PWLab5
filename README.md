# Lab 5 - News site

## Story

Imagine, you're a developer at Newsroom SRL, a local company which runs a site for business news. On a regular meeting you propose to kick-off a new design for the site, as well as newer technologies. Your idea looks nice, but the CTO has requested a proof-of-concept application before main development starts.

## Task

1. Pick a backend framework of your choice;
2. Implement at least 3 roles for site users: `editor`, `subscriber` and anonymous user
3. Implement at least 2 types for news: `public` and `private`
4. Implement the core functions for news site:
  - Editors can create and edit posts;
  - Anybody can access public posts;
  - Subscribers can access private posts.

5. The site has to look nice on both desktop and mobile devices.

## Special conditions

### Node.js students

You have to use Node.js as backend framework, Express, MongoDB and Mongoose technologies. No frontend framework can be used.

### Django students

You have to use Django as backend framework. No frontend framework can be used.

### Others

No frontend framework can be used.

## Grading

Points:
  - basic app where anyone can edit anything - `6` points (`5` points for Django and Node.js students);
  - app with 2 roles - `+1` point;
  - app with 2 types - `+1` point;
  - attractive & responsive design - `+1` point.

You can get `+1` point for implementing `protected` news - before viewing the post, the anonymous visitor should submit a password. Also, you can get `+1` point if news can contain images. You can get `+1` point for a non-trivial functionality.

## Hints

- If you already know a backend framework - use it!
- If you don't, use Ruby on Rails.
- Use SQLite3 as RDBMS, if you're unsure what DBMS to use (why?). Other good choices - PostgreSQL, MongoDB.
- Use CSS libraries for UI part.

