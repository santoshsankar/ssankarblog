Title: Mobile Search & Deep Linking
Date: 2014-06-30 19:35
Category: Product Design
Tags: product design, product development, usability, UI/UX, data, mobile, search, deep linking
Slug: mobile-search-deep-linking
Author: Santosh Sankar
Summary: Putting pen to paper and getting my thoughts out on Google implementing mobile search and app-to-app sharing via deep linking. I explore the points of convenience, app discovery, reinforcing the importance of APIs as well as potential changes to user interactions.

<div style="background-color:#fff;display:inline-block;font-family:'Helvetica Neue',Arial,sans-serif;color:#a7a7a7;font-size:11px;width:100%;max-width:524px;min-width:300px;"><div style="overflow:hidden;position:relative;height:0;padding:62.595420% 0 49px 0;width:100%;"><iframe src="//embed.gettyimages.com/embed/144635375?et=ZtgBDWzcR7tVYH3Sr_s6fA&sig=aS1sHXkRKGuzz68W4u8ofjUuQAwWBO98AslF0T0QW-s=" width="524" height="377" scrolling="no" frameborder="0" style="display:inline-block;position:absolute;top:0;left:0;width:100%;height:100%;"></iframe></div><p style="margin:0;"></p><div style="padding:0;margin:4px 0 0 10px;text-align:left;"><a href="http://www.gettyimages.com/detail/144635375" target="_blank" style="color:#a7a7a7;text-decoration:none;font-weight:normal !important;border:none;display:inline-block;">#144635375</a> / <a href="http://www.gettyimages.com" target="_blank" style="color:#a7a7a7;text-decoration:none;font-weight:normal !important;border:none;display:inline-block;">gettyimages.com</a></div></div>

So all the I/O reviews are out and I assume largely digested. Needless to say, there were some great things unveiled (per usual).  have been thinking and wanted to flesh my thoughts out on search extending into the mobile apps on our phone as well as sharing data amongst apps. At a high level, the feature is enabled by a modified Google crawler that utilizes <a href = "https://developers.google.com/app-indexing/webmasters/app" target = "_blank"> "deep links"</a> that point to specific details within mobile apps. The API can also be used by developers to offer and accept deep linked data among apps. I think this is quite powerful and potentially has broader implications for mobile products.

# The Obvious Convenience
The obvious reason this feature is powerful relates to the convenience as a user. We can simply punch in a query into our search bar and boom, the answer, while likely on the web, is probably much more contextual and relevant if it lies within an app on our phone. For example, say I am in Phoenix and want to eat at the restaurant I was at several months ago. Now I can punch in some descriptors (about the restaurant) into the search bar and voila, it could pop out the name, location and contact of the spot using my OpenTable history. 

In the app-to-app world, I do not need to open an app, do my thing then close it, to open a different app in an effort to continue my workflow. To keep on the restaurant example, let's say I go to eat and decide to share my "food porn" online. I can easily snap a picture and pass it on to Pintrest or Twitter along with location (from my email, calendar or OpenTable) to pin.

## App Discovery
Furthermore, many apps are often downloaded, seldom used and left in the "app graveyard." App search can increase usage and drive down abandonment rates if Google raises an app's importance or relevance through the search bar. Smartphones have not been around for long but the quantity of data we have each personally amassed through increased usage is not news. Google is finally offering a simple, familiar manner by which to tap into it.

# Emphasis on APIs and Interactions
Allowing the ability to sift through the mobile app constellation simply through a search bar could change the way we use mobile apps. Could this be the point where <a href ="https://medium.com/@scottbelsky/the-interface-layer-when-design-commoditizes-tech-e7017872173a?source=tw-80497da4598f-1404146352521" source = "_blank"> apps are rebundled under one interface? </a> If all I need to do is punch a query into the search bar to launch an app-- with context, I will do just that. It seems more efficient than the traditional interactions.

The search bar does not spell doom for apps and shouldn't mean that everything turns into an API but rather it should be viewed as another channel for discovery and even distribution of an app's value. It is great that Google is revealing hidden morsels of value that could otherwise go under the radar. 

## APIs
First and foremost, this highlights the increasing importance of the API given that it facilitates interaction among apps. Of late, you have seen many large players open up and formalize their APIs but also on the flip side, names like Netflix have stepped back and limited their API's functionality. I think it is important for mobile players to offer a rich API to benefit from these new found app searching abilities, app-to-app linking as well as to cultivate an ecosystem around their product.

App-to-app deep Links allows apps to offer and accept Deep Links which in and of itself could create a network effect of sorts. Those apps participating could form connections and drive value to one another. One could even say this blurs the size of the user base since anyone in the Deep Link "network" could benefit from an app's value proposition. The big question likely then turns out to be-- *with a frictionless experience among apps, is there additional value to offer a user?*

## Interactions
On the interaction front, it is important to optimize and realize that users can come through a deep link vs from a launch off the home screen. This brings up a few interesting points-
 
* Can the data from where users are coming from help optimize and improve the UI as well as the UX?
* Are there certain parts of the app that would otherwise go unnoticed since the search bar is in play? In turn, how can that be repositioned?
* With a frictionless experience among apps, is there additional value to offer a user? How does that fit into the current UX?
* Does it allow further innovation of the UI/UX? After all, the seamless interaction between apps requires an app to standout amongst the cohort installed on any given device.

Obviously everyone will have their own opinion but thought it was worthwhile to enumerate my thoughts on the topic. I look forward to see what develops as apps adopt and realize the value of search and intra-app linking.

**Note:** Facebook introduced App Links earlier this year that is a similar service and attempts to place Facebook as a service layer among the various platforms.