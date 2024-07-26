from rest_framework import serializers


# class CouponApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coupon
#         fields = ['code']
class CouponApplySerializer(serializers.Serializer):
    code = serializers.CharField()
