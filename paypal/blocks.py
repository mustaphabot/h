from wagtail import blocks as wagtail_blocks


class PayPalSubscriptionPlanButtonBlock(wagtail_blocks.StructBlock):
    paypal_plan_id = wagtail_blocks.CharBlock(required=True)
    paypal_plan_name = wagtail_blocks.CharBlock(required=True)
    paypal_plan_price = wagtail_blocks.IntegerBlock(required=True)

    class Meta:
        icon = "link"
        template = "paypal/blocks/paypal_subscription_plan_button.html"