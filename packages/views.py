from rest_framework.permissions import IsAuthenticated
from .models import Package, Hotel, Image, Review
from .serializers import PackageSerializer, HotelSerializer, ImageSerializer, ReviewSerializer
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError, NotFound
from .permissions import IsReviewerOrReadOnly, IsAdminOrReadOnly, IsAdminUser
from rest_framework.response import Response


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def list(self, request):
        try:
            packages = Package.objects.all()
            serializer = PackageSerializer(packages, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            package = self.get_object()
            serializer = PackageSerializer(package)
            return Response(serializer.data)
        except Package.DoesNotExist:
            raise NotFound(detail="Package not found")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            package = serializer.save()

            # Handle the hotels after saving the package
            hotels_data = request.data.get('hotels')
            if hotels_data:
                package.hotels.set(hotels_data)
                package.save()

            response_data = serializer.data
            response_data['hotels'] = HotelSerializer(package.hotels.all(), many=True).data

            return Response(response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'validation_error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            package = serializer.save()

            # Handle the hotels after updating the package
            hotels_data = request.data.get('hotels')
            if hotels_data is not None:
                package.hotels.set(hotels_data)
                package.save()

            response_data = serializer.data
            response_data['hotels'] = HotelSerializer(package.hotels.all(), many=True).data

            return Response(response_data)
        except ValidationError as e:
            return Response({'validation_error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Package.DoesNotExist:
            raise NotFound(detail="Package not found")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            package = serializer.save()

            # Handle the hotels after updating the package
            hotels_data = request.data.get('hotels')
            if hotels_data is not None:
                package.hotels.set(hotels_data)
                package.save()

            # response data
            response_data = serializer.data
            response_data['hotels'] = HotelSerializer(package.hotels.all(), many=True).data

            return Response(response_data)
        except ValidationError as e:
            return Response({'validation_error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Package.DoesNotExist:
            raise NotFound(detail="Package not found")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"message": "successfully deleted package"}, status=status.HTTP_204_NO_CONTENT)
        except Package.DoesNotExist:
            raise NotFound(detail="Package not found")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        try:
            hotel_name = request.data.get('name')
            if hotel_name:
                hotel = Hotel.objects.filter(name=hotel_name).exists()
                return Response({'name': 'A hotel with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            hotel = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'validation_error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            hotel_name = request.data.get('name')

            # Check if a hotel with the same name exists (excluding the current instance)
            hotel_queryset = Hotel.objects.filter(name=hotel_name).exclude(pk=instance.pk).exists()
            if hotel_queryset:
                return Response({'name': 'A hotel with this name already exists.'})

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            hotel = serializer.save()
            return Response(serializer.data)
        except ValidationError as e:
            return Response({'validation_error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly, IsReviewerOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsReviewerOrReadOnly, IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Check if the user has already reviewed this package
        package_id = serializer.validated_data['package'].id
        reviewer = self.request.user
        if Review.objects.filter(package_id=package_id, reviewer=reviewer).exists():
            raise ValidationError("You have already reviewed this package.")
        serializer.save(reviewer=reviewer)
