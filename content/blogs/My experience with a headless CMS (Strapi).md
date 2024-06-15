---
title: "My experience with a headless CMS (Strapi)"
date: 2024-01-29T16:54:52Z
tags: ['webdev', 'javascript', 'nextjs', 'strapi']
description: "I was approached by my friend to develop a E-commerce site for his book publishing business. I was..."
canonicalURL: "https://dev.to/abir777/my-experience-with-a-headless-cms-strapi-3j9o"
disableShare: false
searchHidden: false

showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
disableHLJS: false
hideSummary: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true

# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
---

[🔗 dev.to link](https://dev.to/abir777/my-experience-with-a-headless-cms-strapi-3j9o)

I was approached by my friend to develop a E-commerce site for his book publishing business. I was mainly responsible for the back-end part.
Requirements were basic:

- A good looking frontend.
- Multivender (multiple book Publishers / Sellers).
- Admin panel.
- Usual E-commerce stuff: Orders, payments, refunds, shipping, invoice generation etc.

Initially we started off with [next.js](https://nextjs.org/) in the frontend, with [postgresql](https://www.postgresql.org/), [Typeorm](https://typeorm.io/) and [express.js](https://expressjs.com/) in backend.
We knew from day 1 that it might take a huge time to develop, especially the admin panel, so we were looking for alternatives. [**Strapi**](https://strapi.io/) - an Open Source headless CMS was gaining some popularity back then. We gave it a try.

> **tl;dr:** Strapi is an amazing product, but we had some special requirements, which a general CMS couldn't handle, it has some limitations. Thus, we had to change our techstack, but we learnt a lot in the process.

## What is Strapi and what is a headless CMS anyway?

Lets compare it with wordpress, to have easier understanding:

> A headless CMS is a content management system (this part is somewhat similar to wordpress) that stores and manages content but doesn't dictate how it's presented on a website or app. It lets developers pull content through an API to display it however they want (that's where it differs from traditional CMS like Wordpress), giving flexibility in design and platform.

"head" = the front-end presentation layer.

"body" = the back-end content management system.

Now, "head-less" = back-end content management system without the presentation layer. We have to develop the presentation layer ourselves.

[Strapi](https://strapi.io/) is such a headless CMS. There are others in the market like: [Contentful](https://www.contentful.com/), [Sanity](https://www.sanity.io/), [Picocms](https://picocms.org/) etc. We went with the Open Source and most popular one.

## What we appreciate

- It has many [functionalities](https://strapi.io/features) like an admin panel, multiple authentication and authorization methods and a lot more. I have listed a few in this article.
- It also has [good plugins and providers](https://market.strapi.io/) like AWS S3, image optimizers, image uploaders, SEO, editors and it is increasing day-by-day.
- Best of all, it is open source, self-hosted and very [customizable](https://docs.strapi.io/dev-docs/customization). We can customize the admin frontend (GUI) and the backend API as well.

### Content Types

We can define multiple [content types](https://docs.strapi.io/user-docs/content-type-builder): Single types, Collection types and Components.

- **Single type** can be like Footer, Header etc.
- **Collection type** are Posts, Authors, Orders etc.
- Then **Components** are mainly used for dynamic parts of a website like a banner with CTA and image, FAQ, Carousel. We can basically define a whole part of a webpage using components it is very powerful.

> What I learnt is that many sites actually use such CMS in the backend to handle dynamic parts of their site (discounts, banners, CTA), which is mostly set by editors, sales and marketing team.

![Content Types Builder](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9nn1vydcsui5np9qswxq.png)

### Image Optimization

Images can be stored in multiple formats like **large, medium, thumbnail** etc, for faster loading time and all of this is handled by strapi itself using the [file upload](https://docs.strapi.io/dev-docs/plugins/upload) plugin.

On going to: `http://localhost:1337/api/upload/files/1`, we get:

```JSON
{
  "id": 1,
  "name": "query_builder.png",
  "alternativeText": "Query Builder Image",
  "caption": "Query Builder",
  "width": 600,
  "height": 576,
  "formats": {
    "thumbnail": {
      "name": "thumbnail_query_builder.png",
      "hash": "thumbnail_query_builder_7d88426f22",
      "ext": ".png",
      "mime": "image/png",
      "path": null,
      "width": 163,
      "height": 156,
      "size": 12.1,
      "url": "/uploads/thumbnail_query_builder_7d88426f22.png"
    },
    "small": {
      "name": "small_query_builder.png",
      "hash": "small_query_builder_7d88426f22",
      "ext": ".png",
      "mime": "image/png",
      "path": null,
      "width": 500,
      "height": 480,
      "size": 67.21,
      "url": "/uploads/small_query_builder_7d88426f22.png"
    }
  },
  "hash": "query_builder_7d88426f22",
  "ext": ".png",
  "mime": "image/png",
  "size": 13.03,
  "url": "/uploads/query_builder_7d88426f22.png",
  "previewUrl": null,
  "provider": "local",
  "provider_metadata": null,
  "createdAt": "2024-01-28T07:56:48.469Z",
  "updatedAt": "2024-01-28T07:56:48.469Z"
}
```

### API query and filtering

One of the best thing about strapi is their filtering and query functionality, learnt a lot from there. They use the [qs](https://github.com/ljharb/qs) library to handle complex filtering use cases. [See here](https://docs.strapi.io/dev-docs/api/rest/filters-locale-publication). Also, they have a very impressive [query builder](https://docs.strapi.io/dev-docs/api/rest/interactive-query-builder). Probably I will use them in a future complex project.

![Query Builder](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6q94i2a7qvh5zwnwn1fm.png)

There are more such [features](https://strapi.io/features). We listed the ones which we have used.

## Pain points

Most of the bugs we faced is already present in their Github issues.

One of the most surprising bug is that client can update whatever and however they like, even API clients can update id (primary key) of the model. [Related issue](https://github.com/strapi/strapi/issues/19346)

### Type System

Strapi uses [Koa](https://koajs.com/) under the hood. To [customize controllers](https://docs.strapi.io/dev-docs/backend-customization/controllers), you have to work with a `ctx` (context) object. This wasn't clear until you search through the docs properly. They have just mentioned some examples, I hope they just mention that the ctx is from koa in the [Customizing Controllers page](https://docs.strapi.io/dev-docs/backend-customization/controllers), then we could have customized as per our liking. Although this might be a nitpicking (or a skill issue from my side 🙃)

Also, VS Code doesn't provide intellisense even if we use Typescript. You need to install [@types/koa](https://www.npmjs.com/package/@types/koa) to get suggestions.

![Strapi Types](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8c4v6c4ypuo1kwtbgo89.GIF)

### Primary Keys

Anything which isn't alphanumeric can't be primary key (like slug or UUID can't be primary keys). [Related issue](https://github.com/strapi/strapi/issues/1762). This isn't a big issue, we can circumvent this by creating custom controllers.

### JWT Refresh Tokens

JWT tokens are implemented, but there is no refresh token feature as of now (another example of a feature from a forum / [blog](https://strapi.io/blog/how-to-create-a-refresh-token-feature-in-your-strapi-application)). JWT access tokens are expired after 30 days.

### Dead End

We are trying to build a multi-vendor site. The default `User` model wasn't enough. What a typical database schema design would do is just to inherit the `User` model. In SQL database terms it is just to declare a One-to-one field with the `User` model, thus maintaining a relation with the original `User` model.

> Why not just add required fields to the original `User` model itself? No this isn't a scalable schema design. Imagine updating the `User` table constantly if new fields need to be added for seller or customer. This isn't [ACID](https://en.wikipedia.org/wiki/ACID) compliant.

> Can't you just use an altogether different user-defined `User` model? No we can't, strapi is closely tied to its default `User` model, so that it can provide different auth flows effectively. Simple solution is to just define a One-to-One relation with `Seller` and `Customer`.

```JSON
{
  "kind": "collectionType",
  "collectionName": "sellers",
  ...
  "attributes": {
    "description": {
      "type": "text",
      "required": false
    },
    "user": {
      "type": "relation",
      "relation": "oneToOne",
      "target": "plugin::users-permissions.user"
    },
    "books": {
      "type": "relation",
      "relation": "oneToMany",
      "target": "api::book.book",
      "mappedBy": "seller"
    },
    ...
  }
}
```

Strapi has some permission settings through its [permission plugin](https://docs.strapi.io/user-docs/users-roles-permissions).

- We allowed **find and findOne** permission for **sellers**.
- Only **findOne** for **customers**, as usual.
- We only applied **findOne** for **User** model (not **find**, because we don't want clients to enumerate all of our users - obviously).

Here comes the problems:

- `Seller` has `User` as a related field, now the related `User` won't be populated in response, because **find** isn't allowed on users. In fact we can't directly fetch the related `User` from database (bypassing the permission system), due to permissions set earlier - strapi silently excludes the `User` related info.

- You cannot just create a `Seller` instance with a relation to a `User` instance, again for permissions. You must fire another api request just to **"link"** the two models.

- Client (browser) could send related fields like `User`, and it would be updated silently, to fix that add custom code (this isn't a bug - this is definitely expected, just our use case was different).

```Typescript
async update(ctx) {
  // ignore the userId passed from client
  // it is already set while creating
  // (client should not be able to set the userId)
  delete ctx.request.body.data.user;
  return await super.update(ctx);
}
```

## Conclusion

At last, I will thank all the contributors to the strapi project. It is a wonderful project ([Star Here](https://github.com/strapi/strapi)) and I learnt a lot from their work.

They are doing a wonderful work. Open source is mostly a thankless job - where you have to manage a huge community, constant pull requests, feature requests, issues, rewrites and a lot more.

Here I just shared my experience. We observed that this CMS might not be well suited for our project, but strapi has a lot of scope and use cases in various other projects.

We moved on to a different stack altogether (Django + HTMX), why we did that? What about its scalability? How we did that? Stay tuned 😃

Thanks a lot for reading.
Stay safe,
Have a nice day.

