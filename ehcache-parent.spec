
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		ehcache-parent
Version:	2.3
Release:	5.0
License:	GPLv3+
Source0:	ehcache-parent-2.3-5.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/ehcache-parent
BuildArch:	noarch
Summary:	ehcache-parent bootstrap version
Requires:	javapackages-bootstrap
Requires:	java
Requires:	jpackage-utils
Provides:	ehcache-parent = 2.3-5.0:2014.0
Provides:	mvn(net.sf.ehcache:ehcache-parent) = 2.3
Provides:	mvn(net.sf.ehcache:ehcache-parent:pom:) = 2.3

%description
ehcache-parent bootstrap version.

%files
/usr/share/maven-fragments/ehcache-parent
/usr/share/maven-poms/JPP-ehcache-parent.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
