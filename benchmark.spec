#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 6fa3d52
#
Name     : benchmark
Version  : 1.8.4
Release  : 1
URL      : https://github.com/google/benchmark/archive/refs/tags/v1.8.4.tar.gz
Source0  : https://github.com/google/benchmark/archive/refs/tags/v1.8.4.tar.gz
Summary  : Google microbenchmark framework
Group    : Development/Tools
License  : Apache-2.0
Requires: benchmark-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Benchmark
[![build-and-test](https://github.com/google/benchmark/workflows/build-and-test/badge.svg)](https://github.com/google/benchmark/actions?query=workflow%3Abuild-and-test)
[![bazel](https://github.com/google/benchmark/actions/workflows/bazel.yml/badge.svg)](https://github.com/google/benchmark/actions/workflows/bazel.yml)
[![pylint](https://github.com/google/benchmark/workflows/pylint/badge.svg)](https://github.com/google/benchmark/actions?query=workflow%3Apylint)
[![test-bindings](https://github.com/google/benchmark/workflows/test-bindings/badge.svg)](https://github.com/google/benchmark/actions?query=workflow%3Atest-bindings)
[![Coverage Status](https://coveralls.io/repos/google/benchmark/badge.svg)](https://coveralls.io/r/google/benchmark)

%package dev
Summary: dev components for the benchmark package.
Group: Development
Requires: benchmark-lib = %{version}-%{release}
Provides: benchmark-devel = %{version}-%{release}
Requires: benchmark = %{version}-%{release}

%description dev
dev components for the benchmark package.


%package doc
Summary: doc components for the benchmark package.
Group: Documentation

%description doc
doc components for the benchmark package.


%package lib
Summary: lib components for the benchmark package.
Group: Libraries

%description lib
lib components for the benchmark package.


%prep
%setup -q -n benchmark-1.8.4
cd %{_builddir}/benchmark-1.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716794742
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBENCHMARK_ENABLE_GTEST_TESTS=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716794742
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/benchmark/benchmark.h
/usr/include/benchmark/export.h
/usr/lib64/cmake/benchmark/benchmarkConfig.cmake
/usr/lib64/cmake/benchmark/benchmarkConfigVersion.cmake
/usr/lib64/cmake/benchmark/benchmarkTargets-relwithdebinfo.cmake
/usr/lib64/cmake/benchmark/benchmarkTargets.cmake
/usr/lib64/libbenchmark.so
/usr/lib64/libbenchmark_main.so
/usr/lib64/pkgconfig/benchmark.pc
/usr/lib64/pkgconfig/benchmark_main.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/benchmark/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbenchmark.so.0
/usr/lib64/libbenchmark.so.0.0.0
/usr/lib64/libbenchmark_main.so.0
/usr/lib64/libbenchmark_main.so.0.0.0
