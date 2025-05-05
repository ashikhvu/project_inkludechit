from rest_framework import serializers
from app_inkludechit.models import UserProfileModel,User,NomineeModel,ProductModel,PaymentModel
# from django.contrib.auth.models import c
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class NomineeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomineeModel
        fields = '__all__'
    
class ProductModelSerializer(serializers.ModelSerializer):

    joining_date = serializers.DateField(input_formats=['%d-%m-%Y'])
    first_emi_completion_date = serializers.DateField(input_formats=['%d-%m-%Y'])
    last_emi_date = serializers.DateField(input_formats=['%d-%m-%Y'])
    dispatching_committed_date = serializers.DateField(input_formats=['%d-%m-%Y'],required=False,allow_null=True)
    draw_date = serializers.IntegerField(required=False,allow_null=True)
    multi_division_auction_eligibility = serializers.DateField(input_formats=['%d-%m-%Y'],required=False,allow_null=True)

    class Meta:
        model = ProductModel
        fields = '__all__'


class PaymentModelSerializer(serializers.ModelSerializer):

    collection_start_date = serializers.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = PaymentModel
        fields = '__all__'


class UserProfileCreationSerializer(serializers.ModelSerializer):

    nominee_model_data = NomineeModelSerializer()
    product_model_data = ProductModelSerializer()
    payment_model_data = PaymentModelSerializer()

    dob= serializers.DateField(input_formats=['%d-%m-%Y'])
    salary_date= serializers.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = UserProfileModel
        exclude = ['customer_id','user']


    def validate(self,attrs):
        kuri_type=attrs["product_model_data"]["kuri_type"]
        product_code=attrs["product_model_data"]["product_code"]
        document_type=attrs["product_model_data"]["document_type"]
        chit_duration=attrs["product_model_data"]["chit_duration"]
        first_emi_completion_date=attrs["product_model_data"]["first_emi_completion_date"]
        last_emi_date=attrs["product_model_data"]["last_emi_date"]
        auction_eligibility=attrs["product_model_data"]["auction_eligibility"]
        auction_date=attrs["product_model_data"]["auction_date"]
        divident_date=attrs["product_model_data"]["divident_date"]
        if attrs["product_model_data"]["multi_division_auction_eligibility"]:
            multi_division_auction_eligibility= attrs["product_model_data"]["multi_division_auction_eligibility"]
        if attrs["product_model_data"]["multi_division_auction_date"]:
            multi_division_auction_date=attrs["product_model_data"]["multi_division_auction_date"]
        if attrs["product_model_data"]["multi_division_divident_date"]:
            multi_division_divident_date=attrs["product_model_data"]["multi_division_divident_date"]


        draw_date = attrs["product_model_data"]["draw_date"]
        dispatching_committed_date = attrs["product_model_data"]["dispatching_committed_date"]

        if kuri_type == "auction":
            if not product_code in [301,801]:
                raise serializers.ValidationError(f"Product code is invalid it should be either 301 or 801")
            last_date = first_emi_completion_date + relativedelta(months=40)
            if not chit_duration == "40 months":
                raise serializers.ValidationError(f"Chit duration should be 40 months for this selected product")
            if not last_emi_date == last_date:
                raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}")
            
            if product_code == 301:
                if not auction_date == 10 or not divident_date == 9:
                    raise serializers.ValidationError(f"Auction date should be the '10' and divident date should be '9'")
            elif product_code ==801:
                if not auction_date == 8 or not divident_date == 7:
                        raise serializers.ValidationError(f"auction date should be the '8' and divident date should be '7'")
            
            if document_type == "collateral":
                get_date_here = datetime.strptime(str(first_emi_completion_date),"%Y-%m-%d")
                dt = get_date_here.strftime('%B %Y')
                if not auction_eligibility == dt:
                    raise serializers.ValidationError(f"Auction eligilbity date should be '{dt}' ")
            elif document_type == "noncollateral":
                add_month = first_emi_completion_date + relativedelta(months=3)
                get_date_here = datetime.strptime(str(add_month),"%Y-%m-%d")
                dt = get_date_here.strftime("%B %Y")
                if not auction_eligibility == dt:
                    raise serializers.ValidationError(f"Auction eligibility date should be '{dt}' ")
        elif kuri_type == "draw":
            if not product_code in [201,202]:
                raise serializers.ValidationError(f"Product code is invalid it should be either 201 or 202")
            if not chit_duration == "25 months":
                raise serializers.ValidationError(f"Chit duration should be 25 months for this selected product")
            
            last_date = first_emi_completion_date + relativedelta(months=25)
            last_date = last_date.replace(day=15)
            if not last_emi_date == last_date:
                raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}")
            
            if not draw_date == 15:
                raise serializers.ValidationError(f"Draw date should be 15th")
            
        elif kuri_type == "offer":
            if not product_code in [901,902,903,904,951,952]:
                raise serializers.ValidationError(f"Product code is invalid it should be either one of them 901,902,903,904,951,952")

            if product_code in [901,903,904]:
                if not chit_duration == "20 months":
                    raise serializers.ValidationError("Chit duration should be 20 months for this selected product")
                last_date = first_emi_completion_date + relativedelta(months=20)
                if not last_emi_date == last_date:
                    raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}")
                
            elif product_code == 902:
                if not chit_duration == "25 months":
                    raise serializers.ValidationError("Chit duration should be 25 months for this selected product")
                last_date = first_emi_completion_date + relativedelta(months=25)
                if not last_emi_date == last_date:
                    raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}")    
            
            elif product_code in [951,952]:
                if not chit_duration == "40 months":
                    raise serializers.ValidationError("Chit duration should be 40 months for this selected product")
                last_date = first_emi_completion_date + relativedelta(months=40)
                if not last_emi_date == last_date:
                    raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}")
                
            dispatch_date = first_emi_completion_date + relativedelta(months=4)
            if not dispatch_date == dispatching_committed_date:
                raise serializers.ValidationError(f"Dispatching commited date should be '{dispatching_committed_date.strftime("%d-%m-%Y")}'")
            
            div_date = first_emi_completion_date.day
            if not divident_date == div_date :
                raise serializers.ValidationError(f"Divident date should be '{div_date.strftime("%d-%m-%Y")}'")     
        elif kuri_type == "multi division":
            if not product_code == 502:
                raise serializers.ValidationError(f"Product code is invalid it should be 502")
            if not chit_duration == "100 weeks":
                raise serializers.ValidationError("Chit duration should be 100 weeks for this selected product")
            last_date = first_emi_completion_date + relativedelta(weeks=100)
            if not last_emi_date == last_date:
                raise serializers.ValidationError(f"Last emi completion date should be {last_date.strftime("%d-%m-%Y")}") 


            init_day = first_emi_completion_date
            if document_type == "collateral":
                while init_day.weekday() != 4:
                    init_day+= relativedelta(days=1)
            elif document_type == "noncollateral":
                count = 0
                while True:
                    if init_day.weekday() == 4:
                        count +=1
                        if count == 4:
                            break
                    init_day += relativedelta(days=1)

            if multi_division_auction_eligibility == None or multi_division_auction_eligibility == "":
                raise serializers.ValidationError(f"Please provide auction eligibility date ")
            else:
                if not init_day == multi_division_auction_eligibility:
                    raise serializers.ValidationError(f"Auction eligibility date should be '{init_day.strftime("%d-%m-%Y")}' ")

            print(f"{multi_division_auction_date}\t{type(multi_division_auction_date)}")
            if not multi_division_auction_date == "Friday":
                raise serializers.ValidationError(f"Auction date for multi division should be 'Friday' ")
            if not multi_division_divident_date == "Thursday":
                raise serializers.ValidationError(f"Divident date for multi division should be 'Thursday' ")

        return attrs
    
    def create(self,validated_data):
        nominee_data = validated_data.pop('nominee_model_data')
        nominee = NomineeModel.objects.create(**nominee_data)
        product_data = validated_data.pop('product_model_data')
        product = ProductModel.objects.create(**product_data)
        payment_data = validated_data.pop('payment_model_data')
        payment = PaymentModel.objects.create(**payment_data)

        return UserProfileModel.objects.create(
            nominee_model_data=nominee,
            product_model_data=product,
            payment_model_data=payment,
            **validated_data
        )
    

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['nominee_model_data'] = NomineeModelSerializer(instance.nominee_model_data).data
        response['product_model_data'] = ProductModelSerializer(instance.product_model_data).data
        response['payment_model_data'] = PaymentModelSerializer(instance.payment_model_data).data
        return response