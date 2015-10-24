from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from console.login.models import Engine
from .models import Dimensions, Brake, Variant, Capacity, Mileage, Price, Steering, Wheel
from .forms import DimensionForm, EngineForm, BrakeForm, CapacityForm, MileageForm, PriceForm, SteeringForm, WheelForm


class SpecificationView(View):
    def get(self, request, *args, **kwargs):
        variant_id = request.GET.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            dimensions = Dimensions.objects.get(variant=variant)
        except Dimensions.DoesNotExist:
            dimensions = None
        try:
            engine = Engine.objects.get(variant=variant)
        except Engine.DoesNotExist:
            engine = None
        try:
            brake = Brake.objects.get(variant=variant)
        except Brake.DoesNotExist:
            brake = None
        try:
            capacity = Capacity.objects.get(variant=variant)
        except Capacity.DoesNotExist:
            capacity = None
        try:
            mileage = Mileage.objects.get(variant=variant)
        except Mileage.DoesNotExist:
            mileage = None
        try:
            price = Price.objects.get(variant=variant)
        except Price.DoesNotExist:
            price = None
        try:
            steering = Steering.objects.get(variant=variant)
        except Steering.DoesNotExist:
            steering = None
        try:
            wheel = Wheel.objects.get(variant=variant)
        except Wheel.DoesNotExist:
            wheel = None

        return render(request, 'general/specifications.html',
                      {'dimensionsform': DimensionForm, 'engineform': EngineForm, 'brakeform': BrakeForm,
                       'capacityform': CapacityForm, 'mileageform': MileageForm, 'priceform': PriceForm,
                       'steeringform': SteeringForm,
                       'variant': variant, 'price': price, 'steering': steering, 'wheel': wheel, 'wheelform': WheelForm,
                       'dimensions': dimensions, 'engine': engine, 'brake': brake, 'capacity': capacity,
                       'mileage': mileage})

    def post(self, request, *args, **kwargs):
        form = DimensionForm(request.POST)
        variant_id = request.POST.get('variant')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            dimensions = form.save(commit=False)
            dimensions.variant = variant
            dimensions.save()
            messages.success(request, 'Car dimensions added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_dimension(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        dimension = Dimensions.objects.get(variant=variant)
        form = DimensionForm(instance=dimension)
        return render(request, 'general/specificdimension.html', {'form': form, 'variant_id': variant_id})

    def edit_dimension(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        dimension = Dimensions.objects.get(variant=variant)
        form = DimensionForm(request.POST, instance=dimension)
        if form.is_valid():
            dimension = form.save(commit=False)
            dimension.variant = variant
            dimension.save()
            messages.success(request, 'Car dimensions edited.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class EngineView(View):
    def post(self, request, *args, **kwargs):
        form = EngineForm(request.POST)
        variant_id = request.POST.get('variant')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            engine = form.save(commit=False)
            engine.variant = variant
            engine.save()
            messages.success(request, 'Engine details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_engine(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        engine = Engine.objects.get(variant=variant)
        form = EngineForm(instance=engine)
        return render(request, 'general/specificengine.html', {'form': form, 'variant_id': variant_id})

    def edit_engine(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        engine = Engine.objects.get(variant=variant)
        form = EngineForm(request.POST, instance=engine)
        if form.is_valid():
            engine = form.save(commit=False)
            engine.variant = variant
            engine.save()
            messages.success(request, 'Engine specifications changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class BrakeView(View):
    def post(self, request, *args, **kwargs):
        form = BrakeForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            brake = form.save(commit=False)
            brake.variant = variant
            brake.save()
            messages.success(request, 'Brake details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_brake(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        brake = Brake.objects.get(variant=variant)
        form = BrakeForm(instance=brake)
        return render(request, 'general/specificbrake.html', {'form': form, 'variant_id': variant_id})

    def edit_brake(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        brake = Brake.objects.get(variant=variant)
        form = BrakeForm(request.POST, instance=brake)
        if form.is_valid():
            brake = form.save(commit=False)
            brake.variant = variant
            brake.save()
            messages.success(request, 'Brake specifications changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class CapacityView(View):
    def post(self, request, *args, **kwargs):
        form = CapacityForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            capacity = form.save(commit=False)
            capacity.variant = variant
            capacity.save()
            messages.success(request, 'Capacity details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_capacity(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        capacity = Capacity.objects.get(variant=variant)
        form = CapacityForm(instance=capacity)
        return render(request, 'general/specificcapacity.html', {'form': form, 'variant_id': variant_id})

    def edit_capacity(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        capacity = Capacity.objects.get(variant=variant)
        form = CapacityForm(request.POST, instance=capacity)
        if form.is_valid():
            capacity = form.save(commit=False)
            capacity.variant = variant
            capacity.save()
            messages.success(request, 'Capacity details changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class MileageView(View):
    def post(self, request, *args, **kwargs):
        form = MileageForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            mileage = form.save(commit=False)
            mileage.variant = variant
            mileage.save()
            messages.success(request, 'Mileage details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_mileage(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        mileage = Mileage.objects.get(variant=variant)
        form = MileageForm(instance=mileage)
        return render(request, 'general/specificmileage.html', {'form': form, 'variant_id': variant_id})

    def edit_mileage(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        mileage = Mileage.objects.get(variant=variant)
        form = MileageForm(request.POST, instance=mileage)
        if form.is_valid():
            mileage = form.save(commit=False)
            mileage.variant = variant
            mileage.save()
            messages.success(request, 'Mileage details changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))



class PriceView(View):
    def specific_price(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            price = Price.objects.get(variant=variant)
        except Price.DoesNotExist:
            price = None
        form = PriceForm(instance=price)
        return render(request, 'general/specificprice.html', {'form': form, 'variant_id': variant_id})

    def edit_price(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        try:
            price = Price.objects.get(variant=variant)
        except Price.DoesNotExist:
            price = None
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            price = form.save(commit=False)
            price.variant = variant
            price.save()
            messages.success(request, 'Price details changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def post(self, request, *args, **kwargs):
        form = PriceForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            price = form.save(commit=False)
            price.variant = variant
            price.save()
            messages.success(request, 'Price details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class SteeringView(View):
    def post(self, request, *args, **kwargs):
        form = SteeringForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            steering = form.save(commit=False)
            steering.variant = variant
            steering.save()
            messages.success(request, 'Steering details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_steering(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            steering = Steering.objects.get(variant=variant)
        except Steering.DoesNotExist:
            steering = None
        form = SteeringForm(instance=steering)
        return render(request, 'general/specificsteering.html', {'form': form, 'variant_id': variant_id})

    def edit_steering(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        steering = Steering.objects.get(variant=variant)
        form = SteeringForm(request.POST, instance=steering)
        if form.is_valid():
            steering = form.save(commit=False)
            steering.variant = variant
            steering.save()
            messages.success(request, 'Steering details changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))


class WheelView(View):
    def post(self, request, *args, **kwargs):
        form = WheelForm(request.POST)
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            wheel = form.save(commit=False)
            wheel.variant = variant
            wheel.save()
            messages.success(request, 'Wheel details added.')
        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_wheel(self, request, *args, **kwargs):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            wheel = Wheel.objects.get(variant=variant)
        except Wheel.DoesNotExist:
            wheel = None
        form = WheelForm(instance=wheel)
        return render(request, 'general/specificwheel.html', {'form': form, 'variant_id': variant_id})

    def edit_wheel(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        wheel = Wheel.objects.get(variant=variant)
        form = WheelForm(request.POST, instance=wheel)
        if form.is_valid():
            wheel = form.save(commit=False)
            wheel.variant = variant
            wheel.save()
            messages.success(request, 'Wheel details changed.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

