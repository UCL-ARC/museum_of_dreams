# Setting up email notification system for changes on the website

These instructions assume you have purchased a domain name.

I followed the instructions in [this article](https://medium.com/hackernoon/the-easiest-way-to-send-emails-with-django-using-ses-from-aws-62f3d3d33efd). You don't need the seciton on sending from personal emails, but do need the section sending from a domain (that you've purchased).

When you have set up a domain in SES, you need to ensure you have selected "publish to Route 53" so that the details (DKIM) get added to the relevant domain name.

To include it in the admin for select models, I created a mixin which expands the `save_model` function and added the mixin to the admin models. This way, whenever the model is saved in the admin, the researchers should be notified. I also opted to use a template for the html message rather than plain text.

You can view the [code for the mixin](../mod_app/utils/mixins.py) and the [email template](../mod_app/templates/email_template.html)
