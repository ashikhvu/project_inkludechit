class UserProfileCreationSerializer(serializers.ModelSerializer):
    
    # user = UserCreationSerializer(many=True)

    nominee_model_data = NomineeModelSerializer()
    product_model_data = ProductModelSerializer()
    payment_model_data = PaymentModelSerializer()

    class Meta:
        model = UserProfileModel
        exclude = ['customer_id','user']


    # def to_representation(self,instance):
    #     response = super().to_representation(instance)
    #     # response['user'] = UserCreationSerializer(instance.user).data
    #     response['nominee_model_data'] = NomineeModelSerializer(instance.nominee_model_data).data
    #     response['product_model_data'] = ProductModelSerializer(instance.product_model_data).data
    #     response['payment_model_data'] = PaymentModelSerializer(instance.payment_model_data).data
    #     return response




















    def validate(self,attrs):
        kuri_type=attrs["kuri_type"]
        product_code=attrs["product_code"]
        document_type=attrs["document_type"]
        chit_duration=attrs["chit_duration"]
        first_emi_completion_date=attrs["first_emi_completion_date"]
        last_emi_date=attrs["last_emi_date"]
        auction_eligibility=attrs["auction_eligibility"]
        auction_date=attrs["auction_date"]
        divident_date=attrs["divident_date"]

        if kuri_type == "auction":
                if product_code == 301:
                    if document_type == "collateral":
                        new_date = relativedelta(months=40)
                        last_date = first_emi_completion_date + new_date
                        if not chit_duration == 40 or chit_duration == "40":
                            raise serializers.ValidationError(f"Chit duration should be 40 months for this selected product")
                        else:
                            if not last_emi_date == last_date :
                                raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                        get_date_here = datetime.strptime(last_date,"%d/%m%Y")
                        dt = get_date_here.strftime('%B %Y')
                        if not auction_eligibility == dt:
                            raise serializers.ValidationError(f"auction eligilbity date should be {dt}")
                        if auction_date == 10 and divident_date == 9:
                            raise serializers.ValidationError(f"auction date should be the '10' and divident date should be '9'")
                    elif document_type == "noncollateral":
                        new_date = relativedelta(months=40)
                        last_date = first_emi_completion_date + new_date
                        if not chit_duration == 40 or chit_duration == "40":
                            raise serializers.ValidationError(f"Chit duration should be 40 months for this selected product")
                        else:
                            if not last_emi_date == last_date:
                                raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                        last_date += relativedelta(months=3)
                        get_date_here = datetime.strptime(last_date,"%d%m%Y")
                        dt = get_date_here.strftime("%B %Y")
                        if not auction_eligibility == dt:
                            raise serializers.ValidationError(f"Auction eligibility date should be {dt}")
                        if auction_date == 10 and divident_date == 9:
                            raise serializers.ValidationError(f"auction date should be the '10' and divident date should be '9'")
                elif product_code == "801":
                    if document_type == "collateral":
                        new_date = relativedelta(months=40)
                        last_date = first_emi_completion_date + new_date
                        if not chit_duration == 40 or chit_duration == "40":
                            raise serializers.ValidationError(f"Chit duration should be 40 months for this selected product")
                        else:
                            if not last_emi_date == last_date :
                                raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                        get_date_here = datetime.strptime(last_date,"%d/%m%Y")
                        dt = get_date_here.strftime('%B %Y')
                        if not auction_eligibility == dt:
                            raise serializers.ValidationError(f"auction eligilbity date should be {dt}")
                        if auction_date == 10 and divident_date == 9:
                            raise serializers.ValidationError(f"auction date should be the '10' and divident date should be '9'")
                    elif document_type == "noncollateral":
                        new_date = relativedelta(months=40)
                        last_date = first_emi_completion_date + new_date
                        if not chit_duration == 40 or chit_duration == "40":
                            raise serializers.ValidationError(f"Chit duration should be 40 months for this selected product")
                        else:
                            if not last_emi_date == last_date:
                                raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                        last_date += relativedelta(months=3)
                        get_date_here = datetime.strptime(last_date,"%d%m%Y")
                        dt = get_date_here.strftime("%B %Y")
                        if not auction_eligibility == dt:
                            raise serializers.ValidationError(f"Auction eligibility date should be {dt}")
                        if auction_date == 8 and divident_date == 7:
                            raise serializers.ValidationError(f"auction date should be the '8' and divident date should be '7'")


        elif kuri_type == "draw":
            if product_code == "201":
                new_date = relativedelta(months=25)
                last_date = first_emi_completion_date + new_date
                if not chit_duration == 25 or chit_duration == "25":
                    raise serializers.ValidationError(f"Chit duration should be 25 months for this selected product")
                else:
                    if not last_emi_date == last_date:
                        raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                last_date += relativedelta(months=3)
                get_date_here = datetime.strptime(last_date,"%d%m%Y")
                dt = get_date_here.strftime("%B %Y")
                if not auction_eligibility == dt:
                    raise serializers.ValidationError(f"Auction eligibility date should be {dt}")
                if auction_date == 10 and divident_date == 9:
                    raise serializers.ValidationError(f"auction date should be the '10' and divident date should be '9'")
            elif product_code == "202":
                new_date = relativedelta(months=40)
                last_date = first_emi_completion_date + new_date
                if not chit_duration == 40 or chit_duration == "40":
                    raise serializers.ValidationError(f"Chit duration day should be 40 days for this selected product")
                else:
                    if not last_emi_date == last_date:
                        raise serializers.ValidationError(f"Last emi completion date should be {last_date}")
                last_date += relativedelta(months=3)
                get_date_here = datetime.strptime(last_date,"%d%m%Y")
                dt = get_date_here.strftime("%B %Y")
                if not auction_eligibility == dt:
                    raise serializers.ValidationError(f"Auction eligibility date should be {dt}")
                if auction_date == 8 and divident_date == 7:
                    raise serializers.ValidationError(f"auction date should be the '8' and divident date should be '7'")
        elif kuri_type == "offer":
            pass
        elif kuri_type == "multi division":
            pass

        return attrs
    

















    def create(self,validated_data):
        
        # Required fields
        required_fields_here = [
            'agent_code', 'first_name', 'last_name', 'family_name', 'email', 
            'mobile', 'whatsapp', 'place', 'dob', 'pancard_no', 'adhar_no',
            'current_address', 'permenent_address', 'postal_address', 'marital_status',
            'company_address', 'company_pincode', 'designation', 'period_of_work', 
            'working_time', 'salary_date', 'company_salary_mode', 'company_contact_no', 
            'company_reference_mobile_no', 'company_partner_detail', 'bank_name', 
            'amount', 'emi_amount', 'nominee_name', 'nominee_relation', 'nominee_address', 
            'nominee_contact', 'kuri_type', 'product_code', 'document_type', 'collection_mode', 
            'joining_date', 'first_emi_completion_date', 'chit_duration', 'last_emi_date', 
            'auction_eligibility', 'auction_date', 'divident_date', 'draw_date', 
            'dispatching_committed_date', 'payment_mode', 'collection_area', 'collection_point', 
            'collection_start_date', 'customer_committed_day', 'forman_commision', 'upi_number'
        ]

        # Check if all required fields are present and not None or empty
        missing_fields = [field for field in required_fields_here if self.validated_data.get(field) == "" or self.validated_data.get(field) == None ]

        if not missing_fields:
            raise serializers.ValidationError(f"Missing required fields: {', '.join(missing_fields)}")
        else:

            # UserProfileModel
        
            agent_code = self.validated_data['agent_code']
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            family_name = self.validated_data['family_name']
            email = self.validated_data['email']
            mobile = self.validated_data['mobile']
            whatsapp = self.validated_data['whatsapp']
            place = self.validated_data['place']
            dob = self.validated_data['dob']
            pancard_no = self.validated_data['pancard_no']
            adhar_no = self.validated_data['adhar_no']

            current_address = self.validated_data['current_address']
            permenent_address = self.validated_data['permenent_address']
            postal_address = self.validated_data['postal_address']
            marital_status = self.validated_data['marital_status']

            company_address = self.validated_data['company_address']
            company_pincode = self.validated_data['company_pincode']
            designation = self.validated_data['designation']
            period_of_work = self.validated_data['period_of_work']
            working_time = self.validated_data['working_time']
            salary_date = self.validated_data['salary_date']
            company_salary_mode = self.validated_data['company_salary_mode']
            company_contact_no = self.validated_data['company_contact_no']
            company_reference_mobile_no = self.validated_data['company_reference_mobile_no']
            company_partner_detail = self.validated_data['company_partner_detail']

            bank_name = self.validated_data['bank_name']
            amount = self.validated_data['amount']
            emi_amount = self.validated_data['emi_amount']

            
            # nominee_data = validated_data.pop('nominee_model_data')
            # product_data = validated_data.pop('product_model_data')
            # payment_data = validated_data.pop('payment_model_data')

            # # Create UserProfile instance
            # user_profile = UserProfileModel.objects.create(**validated_data)

            # # Create nominee data
            # for nominee in nominee_data:
            #     NomineeModel.objects.create(user_profile=user_profile, **nominee)

            # # Create product data
            # for product in product_data:
            #     ProductModel.objects.create(user_profile=user_profile, **product)

            # # Create payment data
            # for payment in payment_data:
            #     PaymentModel.objects.create(user_profile=user_profile, **payment)

            # return user_profile

        # NomineeModel

            nominee_name = self.validated_data['nominee_name']
            nominee_relation = self.validated_data['nominee_relation']
            nominee_address = self.validated_data['nominee_address']
            nominee_contact = self.validated_data['nominee_contact']

            # ProductModel

            kuri_type = self.validated_data['kuri_type']
            product_code = self.validated_data['product_code']
            document_type = self.validated_data['document_type']
            collection_mode = self.validated_data['collection_mode']
            joining_date = self.validated_data['joining_date']
            first_emi_completion_date = self.validated_data['first_emi_completion_date']
            chit_duration = self.validated_data['chit_duration']
            last_emi_date = self.validated_data['last_emi_date']
            auction_eligibility = self.validated_data['auction_eligibility']
            auction_date = self.validated_data['auction_date']
            divident_date = self.validated_data['divident_date']

            draw_date = self.validated_data['draw_date']
            dispatching_committed_date = self.validated_data['dispatching_committed_date']

            # PaymentModel

            payment_mode = self.validated_data['payment_mode']
            collection_area = self.validated_data['collection_area']
            collection_point = self.validated_data['collection_point']
            collection_start_date = self.validated_data['collection_start_date']
            customer_committed_day = self.validated_data['customer_committed_day']
            forman_commision = self.validated_data['forman_commision']
            upi_number = self.validated_data['upi_number']

            print(agent_code)


        try:
            pass
        except:
            pass
        if True:
            pass
        profile = UserProfileModel.objects.create(

        )
        profile.save()
        return profile
    








     # def validate(self, attrs):
    #     def check_chit_duration(expected_duration):
    #         if str(chit_duration) != str(expected_duration):
    #             raise serializers.ValidationError(f"Chit duration should be {expected_duration} months for this selected product")

    #     def check_last_emi(expected_last_date):
    #         if last_emi_date != expected_last_date:
    #             raise serializers.ValidationError(f"Last emi completion date should be {expected_last_date}")

    #     def check_auction_eligibility(eligibility_base_date):
    #         date_format = "%d/%m%Y" if document_type == "collateral" else "%d%m%Y"
    #         eligibility_date = eligibility_base_date + relativedelta(months=3) if document_type == "noncollateral" else eligibility_base_date
    #         try:
    #             formatted_date = datetime.strptime(eligibility_date.strftime(date_format), date_format).strftime("%B %Y")
    #         except ValueError:
    #             raise serializers.ValidationError("Invalid date format for eligibility date.")
    #         if auction_eligibility != formatted_date:
    #             raise serializers.ValidationError(f"Auction eligibility date should be {formatted_date}")

    #     def check_auction_divident(expected_auction, expected_divident):
    #         if auction_date != expected_auction or divident_date != expected_divident:
    #             raise serializers.ValidationError(f"Auction date should be '{expected_auction}' and divident date should be '{expected_divident}'")

    #     # Extract attributes
    #     kuri_type = attrs["kuri_type"]
    #     product_code = attrs["product_code"]
    #     document_type = attrs["document_type"]
    #     chit_duration = attrs["chit_duration"]
    #     first_emi_completion_date = attrs["first_emi_completion_date"]
    #     last_emi_date = attrs["last_emi_date"]
    #     auction_eligibility = attrs["auction_eligibility"]
    #     auction_date = attrs["auction_date"]
    #     divident_date = attrs["divident_date"]

    #     # Logic grouping by kuri_type and product_code
    #     if kuri_type in ["auction", "draw"]:
    #         product_map = {
    #             "auction": {
    #                 "301": (40, 10, 9),
    #                 "801": (40, 8, 7),
    #             },
    #             "draw": {
    #                 "201": (25, 10, 9),
    #                 "202": (40, 8, 7),
    #             },
    #         }

    #         if product_code in product_map[kuri_type]:
    #             duration, expected_auction_date, expected_divident_date = product_map[kuri_type][product_code]
    #             check_chit_duration(duration)

    #             new_date = relativedelta(months=duration)
    #             expected_last_emi = first_emi_completion_date + new_date
    #             check_last_emi(expected_last_emi)

    #             check_auction_eligibility(expected_last_emi)
    #             check_auction_divident(expected_auction_date, expected_divident_date)

    #     elif kuri_type in ["offer", "multi division"]:
    #         pass  # Add logic as needed